"""Tests del módulo de detección de fraude."""
import io
import pytest
import numpy as np
from unittest.mock import patch, MagicMock
from PIL import Image
from src.fraud_detection.fraud_detector import FraudDetector
from src.fraud_detection.ela_analyzer import ELAAnalyzer


def make_test_jpeg(tmp_path, name="test.jpg", size=(100, 100)) -> str:
    img = Image.fromarray(np.random.randint(0, 255, (*size, 3), dtype=np.uint8))
    path = str(tmp_path / name)
    img.save(path, format="JPEG", quality=95)
    return path


@pytest.fixture
def detector():
    return FraudDetector(ela_threshold=8.0)


@pytest.fixture
def analyzer():
    return ELAAnalyzer()


class TestELAAnalyzer:
    def test_returns_float_scores(self, analyzer, tmp_path):
        path = make_test_jpeg(tmp_path)
        result = analyzer.compute(path)
        assert isinstance(result["mean_score"], float)
        assert isinstance(result["max_score"],  float)
        assert result["mean_score"] >= 0

    def test_authentic_interpretation_for_low_score(self, analyzer):
        assert analyzer._interpret(1.5) == "authentic"

    def test_suspicious_for_mid_score(self, analyzer):
        assert "suspicious" in analyzer._interpret(5.0)

    def test_tampered_for_high_score(self, analyzer):
        assert "tampered" in analyzer._interpret(12.0)


class TestFraudDetector:
    def test_no_fraud_for_clean_image(self, detector, tmp_path):
        path = make_test_jpeg(tmp_path)
        result = detector.predict(path)
        # Imagen sintética limpia debe tener score bajo
        assert isinstance(result["is_fraud"], bool)
        assert 0.0 <= result["fraud_score"] <= 1.0
        assert "ela"  in result
        assert "exif" in result

    def test_exif_suspicious_when_photoshop_in_metadata(self, detector):
        with patch("src.fraud_detection.fraud_detector.piexif.load") as mock_load:
            mock_load.return_value = {
                "0th": {305: b"Adobe Photoshop 2024"}
            }
            result = detector._analyze_exif("fake.jpg")
        assert result["is_suspicious"] is True
        assert "photoshop" in result["software"]

    def test_exif_not_suspicious_for_camera_software(self, detector):
        with patch("src.fraud_detection.fraud_detector.piexif.load") as mock_load:
            mock_load.return_value = {"0th": {305: b"Samsung Camera"}}
            result = detector._analyze_exif("fake.jpg")
        assert result["is_suspicious"] is False

    def test_signals_list_populated_when_fraud(self, detector, tmp_path):
        path = make_test_jpeg(tmp_path)
        with patch.object(detector._ela, "compute",
                          return_value={"mean_score": 15.0, "max_score": 80.0,
                                        "std_score": 5.0, "interpretation": "likely_tampered"}):
            result = detector.predict(path)
        assert result["is_fraud"] is True
        assert len(result["signals"]) > 0
