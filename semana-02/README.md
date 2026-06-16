# Semana 2 — OCR Pipeline: Extracción de Datos del DNI

**Rama:** `feature/s2-ocr-pipeline` → PR hacia `main`

## Entregables
- [ ] `src/ocr/document_scanner.py` — clase DNIScanner completa
- [ ] `src/ocr/image_preprocessor.py` — preprocessing OpenCV (deskew, denoise, binarize)
- [ ] `tests/test_ocr.py` — tests con imágenes sintéticas
- [ ] `OCR_Results.md` — tabla de accuracy por campo del DNI

## OCR_Results.md (completar con tus mediciones)

| Campo DNI | Intentos | Correctos | Accuracy |
|---|---|---|---|
| Número DNI (8 dígitos) | /20 | /20 | % |
| Apellido paterno | /20 | /20 | % |
| Apellido materno | /20 | /20 | % |
| Nombres | /20 | /20 | % |
| Fecha de nacimiento | /20 | /20 | % |
| Fecha de vencimiento | /20 | /20 | % |

## Métricas objetivo
- DNI number: ≥90% accuracy
- Fechas: ≥85% accuracy
- EasyOCR activo como fallback cuando Tesseract retorna < 20 caracteres
