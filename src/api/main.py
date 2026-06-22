from fastapi import FastAPI, UploadFile, File, HTTPException, Request, Depends
import shutil
import os
import uuid
import json
from datetime import datetime

from pydantic import BaseModel
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.ocr.document_scanner import DocumentScanner
from src.ocr.mrz_parser import MRZParser
from src.ocr.dni_parser import DNIParser
from src.ocr.identity_validator import IdentityValidator

from src.face_recognition.face_matcher import FaceMatcher
from src.face_recognition.liveness_detector import LivenessDetector

from src.auth.auth_service import AuthService
from src.auth.jwt_handler import verify_token

app = FastAPI(title="FaceDocVerify API", version="1.0")

UPLOAD_DIR = "temp_uploads"
AUDIT_FILE = "audit_log.jsonl"

os.makedirs(UPLOAD_DIR, exist_ok=True)

security = HTTPBearer()

# =========================
# LOGIN
# =========================
class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/api/v1/login")
def login(data: LoginRequest):
    auth = AuthService()
    result = auth.login(data.username, data.password)

    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return result


# =========================
# JWT VALIDATION
# =========================
def verify_jwt(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = verify_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return payload


# =========================
# RATE LIMIT POR TOKEN (NO POR TIEMPO)
# =========================
TOKEN_LIMIT = 5
token_usage = {}  # {token_sub: count}


def check_token_limit(token_payload: dict):

    user = token_payload.get("sub")

    if user not in token_usage:
        token_usage[user] = 0

    token_usage[user] += 1

    if token_usage[user] > TOKEN_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Token rate limit exceeded. Max 5 requests per token."
        )


# =========================
# VALIDACIÓN ARCHIVOS
# =========================
def validate_file(file: UploadFile):

    ALLOWED_TYPES = ["image/jpeg", "image/png"]
    MAX_FILE_SIZE = 5 * 1024 * 1024

    if file.content_type not in ALLOWED_TYPES:
        return False, "Invalid file type"

    file.file.seek(0, 2)
    size = file.file.tell()
    file.file.seek(0)

    if size > MAX_FILE_SIZE:
        return False, "File too large"

    return True, "OK"


# =========================
# VERIFY IDENTITY (PROTEGIDO)
# =========================
@app.post("/api/v1/verify-identity")
async def verify_identity(
    request: Request,
    front: UploadFile = File(...),
    back: UploadFile = File(...),
    selfie: UploadFile = File(...),
    auth_payload: dict = Depends(verify_jwt)
):

    # 🔥 RATE LIMIT POR TOKEN
    check_token_limit(auth_payload)

    request_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()
    client_ip = request.client.host

    valid_front, _ = validate_file(front)
    valid_back, _ = validate_file(back)
    valid_selfie, _ = validate_file(selfie)

    if not valid_front or not valid_back or not valid_selfie:
        raise HTTPException(status_code=400, detail="Invalid files")

    front_path = f"{UPLOAD_DIR}/front_{request_id}.jpg"
    back_path = f"{UPLOAD_DIR}/back_{request_id}.jpg"
    selfie_path = f"{UPLOAD_DIR}/selfie_{request_id}.jpg"

    with open(front_path, "wb") as f:
        shutil.copyfileobj(front.file, f)

    with open(back_path, "wb") as f:
        shutil.copyfileobj(back.file, f)

    with open(selfie_path, "wb") as f:
        shutil.copyfileobj(selfie.file, f)

    scanner = DocumentScanner()
    front_text = scanner.extract_text(front_path)
    back_text = scanner.extract_text(back_path)

    mrz_data = MRZParser().parse(back_text)
    ocr_data = DNIParser().parse(front_text)
    ocr_data["raw_text"] = front_text

    identity = IdentityValidator().build_final_result(mrz_data, ocr_data)

    matcher = FaceMatcher()
    face_result = matcher.compare_faces(front_path, selfie_path)

    liveness = LivenessDetector().detect_blink(selfie_path)

    access_granted = (
        face_result.get("match", False)
        and liveness.get("live", False)
        and identity.get("documento_vigente", False)
    )

    audit_record = {
        "request_id": request_id,
        "timestamp": timestamp,
        "client_ip": client_ip,
        "user": auth_payload.get("sub"),
        "identity": identity,
        "face_match": face_result,
        "liveness": liveness,
        "access_granted": access_granted
    }

    with open(AUDIT_FILE, "a") as f:
        f.write(json.dumps(audit_record) + "\n")

    try:
        os.remove(front_path)
        os.remove(back_path)
        os.remove(selfie_path)
    except:
        pass

    return {
        "request_id": request_id,
        "identity": identity,
        "face_match": face_result,
        "liveness": liveness,
        "access_granted": access_granted
    }