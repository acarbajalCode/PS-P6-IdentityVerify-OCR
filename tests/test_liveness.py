"""Tests del módulo de liveness detection."""
import numpy as np
import pytest
from src.face_recognition.liveness_detector import LivenessDetector


@pytest.fixture
def detector():
    return LivenessDetector()


def make_frame(value: int, shape=(100, 100, 3)) -> np.ndarray:
    return np.full(shape, value, dtype=np.uint8)


class TestLivenessFromFrames:
    def test_detects_live_when_frames_vary(self, detector):
        # Frames con variación alta → persona real
        frames = [make_frame(i * 20) for i in range(6)]
        result = detector.check_liveness_from_frames(frames)
        assert result["is_live"] is True

    def test_rejects_static_image(self, detector):
        # Todos los frames iguales → foto estática
        frames = [make_frame(128)] * 8
        result = detector.check_liveness_from_frames(frames)
        assert result["is_live"] is False
        assert result["avg_variation"] == pytest.approx(0.0)

    def test_requires_minimum_5_frames(self, detector):
        frames = [make_frame(i * 30) for i in range(3)]
        result = detector.check_liveness_from_frames(frames)
        assert result["is_live"] is False
        assert "Insufficient" in result["reason"]


class TestLivenessFromImage:
    def test_rejects_blank_image(self, detector, tmp_path):
        import cv2
        blank = np.zeros((200, 200), dtype=np.uint8)
        path = str(tmp_path / "blank.jpg")
        cv2.imwrite(path, blank)

        result = detector.check_liveness_from_image(path)
        # Laplacian de imagen uniforme ≈ 0 → baja nitidez → rechazado
        assert result["laplacian_var"] < detector.LAPLACIAN_THRESHOLD

    def test_error_on_missing_file(self, detector):
        result = detector.check_liveness_from_image("/no/existe.jpg")
        assert result["is_live"] is False
        assert "Cannot read" in result["reason"]
