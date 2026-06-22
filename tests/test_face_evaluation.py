import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from face_recognition.face_matcher import FaceMatcher

print("===================================")
print("FACE EVALUATION - SEMANA 3")
print("===================================")

matcher = FaceMatcher(model_name="ArcFace")

# =========================
# DATASET
# =========================
pairs_true = [
    ("tests/fixtures/dni_face1.jpeg", "tests/fixtures/selfie1_other.jpeg"),
    ("tests/fixtures/dni_face2.jpeg", "tests/fixtures/selfie2.jpeg"),
    ("tests/fixtures/dni_face3.jpeg", "tests/fixtures/selfie3.jpeg"),
]

pairs_false = [
    ("tests/fixtures/dni_face1.jpeg", "tests/fixtures/selfie2.jpeg"),
    ("tests/fixtures/dni_face2.jpeg", "tests/fixtures/selfie3.jpeg"),
    ("tests/fixtures/dni_face3.jpeg", "tests/fixtures/selfie1.jpeg"),
]

# =========================
# RESULTADOS
# =========================
true_scores = []
false_scores = []

print("\n--- TRUE MATCHES ---")
for a, b in pairs_true:
    r = matcher.compare_faces(a, b)
    print(r)
    true_scores.append(r["distance"])

print("\n--- FALSE MATCHES ---")
for a, b in pairs_false:
    r = matcher.compare_faces(a, b)
    print(r)
    false_scores.append(r["distance"])

# =========================
# MÉTRICAS BÁSICAS
# =========================
avg_true = sum(true_scores) / len(true_scores)
avg_false = sum(false_scores) / len(false_scores)

print("\n===================================")
print("SUMMARY METRICS")
print("===================================")

print(f"Avg TRUE distance : {avg_true:.3f}")
print(f"Avg FALSE distance: {avg_false:.3f}")

# regla simple de separación
accuracy = 100 if avg_true < avg_false else 0

print(f"Separation Quality: {accuracy}%")