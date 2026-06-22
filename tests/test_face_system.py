import sys
import os

# =========================
# AGREGAR SRC AL PATH
# =========================
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from face_recognition.face_matcher import FaceMatcher
from face_recognition.liveness_detector import LivenessDetector

print("===================================")
print("FACE SYSTEM TEST (LIVENESS + MATCH)")
print("===================================")

# =========================
# RUTAS DE PRUEBA
# =========================
SELFIE_PATH = "tests/fixtures/selfie1.jpeg"
ID_FACE_PATH = "tests/fixtures/dni_face1.jpeg"

# =========================
# 1. LIVENESS CHECK
# =========================
liveness = LivenessDetector().detect_blink(SELFIE_PATH)

print("\n--- LIVENESS RESULT ---")
print(liveness)

if not liveness["live"]:
    print("\n❌ ACCESS DENIED: Fake or invalid face detected")
    sys.exit(0)

# =========================
# 2. FACE MATCHING
# =========================
matcher = FaceMatcher(model_name="ArcFace")

match_result = matcher.compare_faces(
    SELFIE_PATH,
    ID_FACE_PATH
)

print("\n--- FACE MATCH RESULT ---")
print(match_result)

# =========================
# 3. DECISIÓN FINAL
# =========================
if match_result.get("match"):
    print("\n✅ ACCESS GRANTED: Identity verified")
else:
    print("\n❌ ACCESS DENIED: Face mismatch")