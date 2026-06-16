# Semana 3 — Reconocimiento Facial + Liveness Detection

**Rama:** `feature/s3-face-recognition` → PR hacia `main`

## Entregables
- [ ] `src/face_recognition/face_matcher.py` — clase FaceMatcher con DeepFace
- [ ] `src/face_recognition/liveness_detector.py` — detector de ataques de presentación
- [ ] `tests/test_face_matcher.py`
- [ ] `Face_Results.md` — accuracy del face matching con dataset sintético

## Face_Results.md (completar)

| Modelo | True Match (similarity) | False Match (similarity) | Threshold | Accuracy |
|---|---|---|---|---|
| VGG-Face | | | 0.80 | % |
| Facenet512 | | | 0.80 | % |
| ArcFace | | | 0.80 | % |
| **Ensemble** | | | 0.80 | % |

## Liveness Results

| Tipo de ataque | Detectado | No detectado | Accuracy |
|---|---|---|---|
| Foto impresa en papel | /10 | /10 | % |
| Foto en pantalla de celular | /10 | /10 | % |
| Video grabado (replay) | /10 | /10 | % |

## Métricas objetivo
- Face matching accuracy: ≥85%
- Liveness detection: ≥85% (rechaza fotos/pantallas)
