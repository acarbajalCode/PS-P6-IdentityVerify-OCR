import os
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from fastapi import HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials


SECRET_KEY  = os.getenv("SECRET_KEY", "CHANGE_THIS_IN_ENV")
ALGORITHM   = os.getenv("JWT_ALGORITHM", "HS256")
EXPIRE_MIN  = int(os.getenv("JWT_EXPIRE_MINUTES", "15"))


class JWTHandler:
    """Gestión segura de tokens JWT para la API UQ·VerifyID."""

    def create_token(self, subject: str, extra_claims: dict | None = None) -> str:
        now = datetime.now(timezone.utc)
        payload = {
            "sub": subject,
            "iat": now,
            "exp": now + timedelta(minutes=EXPIRE_MIN),
        }
        if extra_claims:
            payload.update(extra_claims)
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    def verify_token(self, token: str) -> dict:
        try:
            return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Invalid or expired token: {e}",
                headers={"WWW-Authenticate": "Bearer"},
            )


# Instancia singleton para importar directamente
_handler = JWTHandler()
create_access_token = _handler.create_token
verify_token        = _handler.verify_token


def get_current_user(credentials: HTTPAuthorizationCredentials) -> dict:
    """Dependencia FastAPI para proteger endpoints con JWT."""
    return verify_token(credentials.credentials)
