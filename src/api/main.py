from fastapi import FastAPI
from .routes import router
from .security import configure_security

app = FastAPI(
    title       = "UQ·VerifyID — Secure Identity Verification API",
    description = (
        "Pipeline multi-modal de verificación de identidad: OCR del DNI peruano + "
        "reconocimiento facial (DeepFace) + detección de fraude documental (ELA + EXIF). "
        "DD281 Programación Segura — Universidad Autónoma del Perú — 2026-1."
    ),
    version     = "1.0.0",
    docs_url    = "/docs",
    redoc_url   = "/redoc",
)

configure_security(app)
app.include_router(router, prefix="/api/v1")


@app.get("/health", tags=["System"])
async def health():
    return {"status": "ok", "service": "UQ·VerifyID", "version": "1.0.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)
