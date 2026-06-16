import os
import uuid
import time
import tempfile
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.auth.jwt_handler import get_current_user
from src.ocr.document_scanner import DNIScanner
from src.face_recognition.face_matcher import FaceMatcher
from src.face_recognition.liveness_detector import LivenessDetector
from src.fraud_detection.fraud_detector import FraudDetector
from .security import limiter

router   = APIRouter()
security = HTTPBearer()

_scanner  = DNIScanner()
_matcher  = FaceMatcher()
_liveness = LivenessDetector()
_fraud    = FraudDetector()

ALLOWED_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


async def _save_temp(upload: UploadFile, tmp_dir: str, prefix: str) -> str:
    content = await upload.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(413, "File too large — max 5 MB")

    if upload.content_type not in ALLOWED_TYPES:
        raise HTTPException(415, f"Unsupported media type: {upload.content_type}")

    path = os.path.join(tmp_dir, f"{prefix}_{uuid.uuid4().hex}.jpg")
    with open(path, "wb") as f:
        f.write(content)
    return path


@router.post("/verify-identity", summary="Verificar identidad: OCR + Face + Fraud")
@limiter.limit("5/minute")
async def verify_identity(
    request,
    document: UploadFile = File(..., description="Foto del DNI (JPG/PNG, máx 5 MB)"),
    selfie:   UploadFile = File(..., description="Selfie del usuario (JPG/PNG, máx 5 MB)"),
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    get_current_user(credentials)   # Valida JWT — lanza 401 si es inválido

    request_id = str(uuid.uuid4())
    start_time = time.time()
    tmp_dir    = tempfile.mkdtemp()
    doc_path   = None
    self_path  = None

    try:
        doc_path  = await _save_temp(document, tmp_dir, "doc")
        self_path = await _save_temp(selfie,   tmp_dir, "self")

        ocr_result   = _scanner.extract_dni_fields(doc_path)
        face_result  = _matcher.verify_identity(self_path, doc_path)
        fraud_result = _fraud.predict(doc_path)
        live_result  = _liveness.check_liveness_from_image(self_path)

        elapsed_ms = round((time.time() - start_time) * 1000)

        overall_approved = (
            ocr_result["valid"]
            and face_result["match"]
            and not fraud_result["is_fraud"]
            and live_result["is_live"]
        )

        return {
            "request_id":        request_id,
            "approved":          overall_approved,
            "processing_time_ms": elapsed_ms,
            "ocr":               ocr_result,
            "face":              face_result,
            "fraud":             fraud_result,
            "liveness":          live_result,
        }

    finally:
        # Siempre borrar imágenes temporales (OWASP A05 — no datos sensibles en disco)
        for path in [doc_path, self_path]:
            if path and os.path.exists(path):
                os.remove(path)
        if os.path.isdir(tmp_dir):
            try:
                os.rmdir(tmp_dir)
            except OSError:
                pass


@router.post("/token", summary="Obtener JWT de prueba (solo desarrollo)")
async def get_test_token():
    if os.getenv("APP_ENV", "development") == "production":
        raise HTTPException(403, "Token endpoint disabled in production")
    from src.auth.jwt_handler import create_access_token
    return {"access_token": create_access_token("test-user"), "token_type": "bearer"}
