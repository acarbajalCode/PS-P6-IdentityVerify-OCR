# API Reference — UQ·VerifyID

Base URL: `https://verifyid.uqaisolutions.com.pe/api/v1`  
Documentación interactiva: `GET /docs` (Swagger UI)

---

## Autenticación

Todos los endpoints (excepto `/health` y `/token`) requieren JWT en el header:

```
Authorization: Bearer <token>
```

---

## Endpoints

### POST /verify-identity

Ejecuta el pipeline completo: OCR + Face Matching + Liveness + Fraud Detection.

**Rate limit:** 5 solicitudes por minuto por IP.

**Request:** `multipart/form-data`

| Campo | Tipo | Requerido | Descripción |
|---|---|:---:|---|
| `document` | file (JPG/PNG) | ✅ | Foto del DNI peruano, máx 5 MB |
| `selfie` | file (JPG/PNG) | ✅ | Selfie del usuario, máx 5 MB |

**Response 200:**
```json
{
  "request_id": "uuid",
  "approved": true,
  "processing_time_ms": 1230,
  "ocr": {
    "valid": true,
    "dni_number": "12345678",
    "apellido_paterno": "GARCIA",
    "apellido_materno": "LOPEZ",
    "nombre": "MARIA",
    "fecha_nac": "01/01/1990",
    "fecha_venc": "31/12/2030",
    "method_used": "tesseract"
  },
  "face": {
    "match": true,
    "similarity": 0.87,
    "threshold": 0.8,
    "models_used": 3,
    "error": null
  },
  "fraud": {
    "is_fraud": false,
    "fraud_score": 0.02,
    "signals": []
  },
  "liveness": {
    "is_live": true,
    "laplacian_var": 145.3,
    "reason": "Sharpness within expected range for real selfie"
  }
}
```

**Errores:**

| Código | Causa |
|---|---|
| 401 | JWT inválido o expirado |
| 413 | Archivo mayor a 5 MB |
| 415 | Tipo de archivo no soportado (solo JPG/PNG) |
| 429 | Rate limit excedido — esperar 60 segundos |

---

### GET /health

Verificación del estado del servicio. No requiere autenticación.

**Response 200:**
```json
{"status": "ok", "service": "UQ·VerifyID", "version": "1.0.0"}
```

---

### POST /token *(solo desarrollo)*

Genera un JWT de prueba. Deshabilitado en producción.

**Response 200:**
```json
{"access_token": "eyJ...", "token_type": "bearer"}
```

---

## Ejemplo cURL completo

```bash
# 1. Obtener token (desarrollo)
TOKEN=$(curl -s -X POST http://localhost:8000/api/v1/token | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")

# 2. Verificar identidad
curl -X POST http://localhost:8000/api/v1/verify-identity \
  -H "Authorization: Bearer $TOKEN" \
  -F "document=@tests/fixtures/synthetic_dni_001.jpg" \
  -F "selfie=@tests/fixtures/synthetic_selfie_001.jpg" \
  | python3 -m json.tool
```
