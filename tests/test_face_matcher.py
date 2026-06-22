import sys
import os

# 🔥 FIX DEFINITIVO
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from face_recognition.face_matcher import FaceMatcher


print("=== FACE MATCH TEST ===")

matcher = FaceMatcher()

result = matcher.compare_faces(
    "tests/fixtures/selfie1.jpeg",
    "tests/fixtures/dni_face1.jpeg"
)

print(result)