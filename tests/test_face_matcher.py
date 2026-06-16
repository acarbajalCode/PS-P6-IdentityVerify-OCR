"""Tests del módulo de reconocimiento facial — FaceMatcher."""
import pytest
from unittest.mock import patch, MagicMock
from src.face_recognition.face_matcher import FaceMatcher


@pytest.fixture
def matcher():
    return FaceMatcher()


class TestVerifyIdentity:
    @patch("src.face_recognition.face_matcher.DeepFace.verify")
    def test_match_when_similarity_above_threshold(self, mock_verify, matcher):
        # distance 0.10 → similarity 0.90 → match
        mock_verify.return_value = {"distance": 0.10, "verified": True}

        result = matcher.verify_identity("selfie.jpg", "doc_photo.jpg")

        assert result["match"]       is True
        assert result["similarity"]  >= matcher.SIMILARITY_THRESHOLD
        assert result["models_used"] == len(matcher.MODELS)

    @patch("src.face_recognition.face_matcher.DeepFace.verify")
    def test_no_match_when_distance_too_high(self, mock_verify, matcher):
        # distance 0.30 → similarity 0.70 → no match
        mock_verify.return_value = {"distance": 0.30, "verified": False}

        result = matcher.verify_identity("selfie.jpg", "doc_photo.jpg")

        assert result["match"]      is False
        assert result["similarity"] < matcher.SIMILARITY_THRESHOLD

    @patch("src.face_recognition.face_matcher.DeepFace.verify",
           side_effect=Exception("No face detected"))
    def test_returns_error_when_no_face(self, mock_verify, matcher):
        result = matcher.verify_identity("blank.jpg", "blank.jpg")

        assert result["match"]       is False
        assert result["models_used"] == 0
        assert result["error"]       is not None

    @patch("src.face_recognition.face_matcher.DeepFace.verify")
    def test_ensemble_uses_average_distance(self, mock_verify, matcher):
        # Simular 3 modelos con distancias diferentes
        mock_verify.side_effect = [
            {"distance": 0.10},
            {"distance": 0.12},
            {"distance": 0.14},
        ]
        result = matcher.verify_identity("s.jpg", "d.jpg")
        expected_similarity = round(1.0 - (0.10 + 0.12 + 0.14) / 3, 4)
        assert result["similarity"] == expected_similarity
