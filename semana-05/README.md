# Semana 5 — Fraud Detection: Detección de Documentos Falsificados

**Rama:** `feature/s5-fraud-detection` → PR hacia `main`

## Entregables
- [ ] `src/fraud_detection/fraud_detector.py` — clase FraudDetector completa
- [ ] `src/fraud_detection/ela_analyzer.py` — Error Level Analysis
- [ ] `tests/test_fraud_detector.py`
- [ ] `Fraud_Model_Metrics.md` — métricas del clasificador

## Fraud_Model_Metrics.md (completar con tus mediciones)

| Métrica | Valor obtenido | Objetivo |
|---|---|---|
| Accuracy | % | ≥85% |
| Precision | % | ≥80% |
| Recall | % | ≥80% |
| F1-Score | % | ≥80% |
| AUC-ROC | | ≥0.85 |

## Dataset de entrenamiento (sintético)

| Clase | Cantidad |
|---|---|
| Documentos auténticos (sintéticos) | 50 |
| Documentos alterados en Photoshop | 25 |
| Documentos alterados en GIMP | 25 |

## ELA Score Reference

| ELA Score | Interpretación |
|---|---|
| 0 - 3.0 | Documento auténtico |
| 3.0 - 8.0 | Zona gris — revisar EXIF |
| 8.0+ | Posible alteración detectada |
