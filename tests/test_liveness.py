import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from face_recognition.liveness_detector import LivenessDetector

print("=== LIVENESS TEST ===")

detector = LivenessDetector()

result = detector.detect_blink(
    "tests/fixtures/selfie1.jpeg"
)

print(result)