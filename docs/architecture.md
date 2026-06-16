# Arquitectura del Sistema — UQ·VerifyID

## Diagrama de componentes

```
┌──────────────────────────────────────────────────────────────────┐
│                        CLIENTE                                    │
│  App web / Mobile  →  HTTPS (TLS 1.3)  →  JWT en header         │
└───────────────────────────────┬──────────────────────────────────┘
                                │
┌───────────────────────────────▼──────────────────────────────────┐
│               AZURE APP SERVICES (westus3)                        │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │              FastAPI Application                             │ │
│  │                                                             │ │
│  │  ① JWT Validation (src/auth/jwt_handler.py)                │ │
│  │  ② Rate Limiting — 5 req/min/IP (slowapi)                  │ │
│  │  ③ File Validation — tipo + tamaño                         │ │
│  │                                                             │ │
│  │  ┌──────────┐  ┌──────────────┐  ┌──────────────────────┐ │ │
│  │  │   OCR    │  │ Face Matcher │  │   Fraud Detector     │ │ │
│  │  │Tesseract │  │  DeepFace    │  │  ELA + EXIF +        │ │ │
│  │  │EasyOCR   │  │  VGG-Face2  │  │  XGBoost (S5)        │ │ │
│  │  │OpenCV    │  │  Facenet512  │  │                      │ │ │
│  │  │          │  │  ArcFace     │  │  Liveness Detector   │ │ │
│  │  └──────────┘  └──────────────┘  │  OpenCV Laplacian    │ │ │
│  │                                   └──────────────────────┘ │ │
│  │  ④ Borrado de imágenes temporales (finally block)          │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌───────────────┐  ┌──────────────────┐  ┌──────────────────┐  │
│  │ Azure Blob    │  │  Azure Key Vault  │  │ Azure PostgreSQL │  │
│  │ (imágenes     │  │  (SECRET_KEY,     │  │ (resultados de   │  │
│  │  AES-256)     │  │   DB conn str)    │  │  verificación)   │  │
│  └───────────────┘  └──────────────────┘  └──────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

## Pipeline de verificación (flujo de datos)

```
Imagen DNI  ──► Preprocessing (OpenCV) ──► Tesseract OCR ──► Parse campos
                                                    │
                                              EasyOCR (fallback)

Selfie      ──► Liveness check (Laplacian) ──► DeepFace verify ──► similarity score
                                                    │
                                              ensemble 3 modelos

Imagen DNI  ──► ELA Analysis ──► EXIF check ──► fraud_score + signals
```

## Decisiones de seguridad

| Decisión | Alternativa rechazada | Razón |
|---|---|---|
| Imágenes en tmp borradas después del proceso | Guardar en Blob para re-análisis | Principio de mínima retención de datos |
| SECRET_KEY desde Azure Key Vault | Hardcodeada en código | Secretos no deben estar en control de versiones |
| Rate limiting 5/min | Sin límite | Previene abuso de API y DoS |
| JWT expiración 15 min | Tokens de larga duración | Reduce ventana de ataque si se roba un token |
| TLS 1.3 forzado | HTTP | Las imágenes de DNI son datos sensibles |
| Ensemble 3 modelos face | Un solo modelo | Mayor robustez, reduce falsos positivos/negativos |
