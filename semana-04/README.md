# Semana 4 ★ — EXPOSICIÓN PARCIAL (EP) — 60%

**Rama:** `feature/s4-ep-integration` → PR hacia `main`

## Entregables EP
- [ ] `src/api/main.py` — endpoint `/api/v1/verify-identity` funcional
- [ ] Demo: DNI sintético → OCR → Face Match → JSON resultado
- [ ] Imágenes temporales eliminadas después del proceso (verificar con logs)
- [ ] API corriendo en localhost:8000 con documentación en /docs

## Demo Script (ejecutar en la presentación)

```bash
# Terminal 1: Levantar API
uvicorn src.api.main:app --reload --port 8000

# Terminal 2: Probar endpoint
curl -X POST http://localhost:8000/api/v1/verify-identity \
  -H "Authorization: Bearer TU_JWT_TOKEN" \
  -F "document=@tests/fixtures/synthetic_dni_001.jpg" \
  -F "selfie=@tests/fixtures/synthetic_selfie_001.jpg"
```

## Resultado esperado

```json
{
  "request_id": "uuid-aqui",
  "document_valid": true,
  "dni_number": "12345678",
  "face_match": true,
  "similarity": 0.87,
  "is_fraud": false,
  "processing_time_ms": 1234
}
```

## Checklist EP

- [ ] OCR extrae DNI number con ≥90% accuracy
- [ ] Face matching retorna similarity score numérico
- [ ] Los archivos temporales se eliminan (verificar con `ls /tmp/`)
- [ ] La API tiene JWT activo (sin token → 401)
