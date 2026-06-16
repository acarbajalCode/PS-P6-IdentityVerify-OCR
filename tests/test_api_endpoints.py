"""Tests de integración de los endpoints FastAPI."""
import io
import pytest
import numpy as np
from PIL import Image
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from src.api.main import app
from src.auth.jwt_handler import create_access_token

client = TestClient(app, raise_server_exceptions=False)


def _make_jpeg_bytes() -> bytes:
    arr = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
    buf = io.BytesIO()
    Image.fromarray(arr).save(buf, format="JPEG")
    return buf.getvalue()


def _auth_headers() -> dict:
    token = create_access_token("test-user")
    return {"Authorization": f"Bearer {token}"}


class TestHealthEndpoint:
    def test_health_returns_200(self):
        resp = client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"


class TestTokenEndpoint:
    def test_get_test_token_in_dev(self):
        resp = client.post("/api/v1/token")
        assert resp.status_code == 200
        assert "access_token" in resp.json()


class TestVerifyIdentityEndpoint:
    def test_returns_401_without_token(self):
        img = _make_jpeg_bytes()
        resp = client.post(
            "/api/v1/verify-identity",
            files={
                "document": ("doc.jpg", img, "image/jpeg"),
                "selfie":   ("selfie.jpg", img, "image/jpeg"),
            },
        )
        assert resp.status_code == 401

    @patch("src.api.routes._scanner")
    @patch("src.api.routes._matcher")
    @patch("src.api.routes._fraud")
    @patch("src.api.routes._liveness")
    def test_full_pipeline_returns_result(self, mock_live, mock_fraud,
                                          mock_match, mock_scan):
        mock_scan.extract_dni_fields.return_value = {
            "valid": True, "dni_number": "12345678",
            "fecha_nac": "01/01/1990", "fecha_venc": "31/12/2030",
            "raw_text": "...", "method_used": "tesseract",
        }
        mock_match.verify_identity.return_value = {
            "match": True, "similarity": 0.91,
            "threshold": 0.80, "models_used": 3, "error": None,
        }
        mock_fraud.predict.return_value = {
            "is_fraud": False, "fraud_score": 0.02,
            "ela": {}, "exif": {}, "signals": [],
        }
        mock_live.check_liveness_from_image.return_value = {
            "is_live": True, "laplacian_var": 120.5, "reason": "OK",
        }

        img = _make_jpeg_bytes()
        resp = client.post(
            "/api/v1/verify-identity",
            headers=_auth_headers(),
            files={
                "document": ("doc.jpg",    img, "image/jpeg"),
                "selfie":   ("selfie.jpg", img, "image/jpeg"),
            },
        )
        assert resp.status_code == 200
        body = resp.json()
        assert "request_id" in body
        assert "approved"   in body
        assert body["ocr"]["dni_number"] == "12345678"
        assert body["face"]["match"]     is True

    def test_rejects_oversized_file(self):
        big_file = b"x" * (6 * 1024 * 1024)  # 6 MB > límite de 5 MB
        resp = client.post(
            "/api/v1/verify-identity",
            headers=_auth_headers(),
            files={
                "document": ("big.jpg", big_file, "image/jpeg"),
                "selfie":   ("s.jpg",   b"small", "image/jpeg"),
            },
        )
        assert resp.status_code == 413
