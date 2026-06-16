import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse


limiter = Limiter(key_func=get_remote_address)


def configure_security(app: FastAPI) -> None:
    """Aplica todas las capas de seguridad HTTP a la aplicación FastAPI."""

    allowed_origins = os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost:3000,http://localhost:8000",
    ).split(",")

    app.add_middleware(
        CORSMiddleware,
        allow_origins  = allowed_origins,
        allow_methods  = ["GET", "POST"],
        allow_headers  = ["Authorization", "Content-Type"],
        allow_credentials = False,
    )

    # Rate limiting global
    app.state.limiter = limiter
    app.add_middleware(SlowAPIMiddleware)

    @app.exception_handler(RateLimitExceeded)
    async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
        return JSONResponse(
            status_code=429,
            content={"detail": "Too many requests — retry after 60 seconds"},
        )

    # Security headers en todas las respuestas
    @app.middleware("http")
    async def add_security_headers(request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"]    = "nosniff"
        response.headers["X-Frame-Options"]           = "DENY"
        response.headers["X-XSS-Protection"]         = "1; mode=block"
        response.headers["Referrer-Policy"]           = "strict-origin-when-cross-origin"
        response.headers["Content-Security-Policy"]   = "default-src 'self'"
        response.headers["Permissions-Policy"]        = "camera=(), microphone=(), geolocation=()"
        if os.getenv("APP_ENV", "development") == "production":
            response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        return response
