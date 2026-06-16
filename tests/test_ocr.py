"""Tests del módulo OCR — DNIScanner e ImagePreprocessor."""
import re
import pytest
from unittest.mock import patch, MagicMock
from src.ocr.document_scanner import DNIScanner


@pytest.fixture
def scanner():
    return DNIScanner()


class TestDNINumberExtraction:
    def test_extracts_8_digit_dni(self, scanner):
        text = "REPÚBLICA DEL PERÚ\nDNI\n12345678\nJUAN PEREZ"
        result = scanner._extract_dni_number(text)
        assert result == "12345678"

    def test_ignores_7_digit_number(self, scanner):
        result = scanner._extract_dni_number("número 1234567 aquí")
        assert result is None

    def test_ignores_9_digit_number(self, scanner):
        result = scanner._extract_dni_number("número 123456789 aquí")
        assert result is None

    def test_returns_first_match_when_multiple(self, scanner):
        result = scanner._extract_dni_number("12345678 y también 87654321")
        assert result == "12345678"


class TestFieldParsing:
    def test_parse_with_dates(self, scanner):
        text = "12345678 APELLIDO MATERNO NOMBRE 15/06/1995 31/12/2030"
        result = scanner._parse_fields(text)
        assert result["dni_number"]  == "12345678"
        assert result["fecha_nac"]   == "15/06/1995"
        assert result["fecha_venc"]  == "31/12/2030"

    def test_valid_flag_true_when_dni_and_date_present(self, scanner):
        text = "12345678 fecha 01/01/2000"
        fields = scanner._parse_fields(text)
        # valid se asigna fuera en extract_dni_fields, aquí verificamos lógica interna
        assert fields["dni_number"] is not None
        assert fields["fecha_nac"] is not None

    def test_none_fields_when_no_match(self, scanner):
        fields = scanner._parse_fields("texto sin datos")
        assert fields["dni_number"] is None
        assert fields["fecha_nac"] is None


class TestExtractDNIFields:
    @patch("src.ocr.document_scanner.pytesseract.image_to_string")
    @patch("src.ocr.document_scanner.ImagePreprocessor.preprocess")
    def test_uses_tesseract_when_text_long_enough(self, mock_pre, mock_tess, scanner):
        mock_pre.return_value = MagicMock()
        mock_tess.return_value = "12345678 GARCIA LOPEZ MARIA 01/01/1990 31/12/2030"

        result = scanner.extract_dni_fields("fake_path.jpg")

        assert result["method_used"]  == "tesseract"
        assert result["dni_number"]   == "12345678"
        assert result["valid"]        is True

    @patch("src.ocr.document_scanner.pytesseract.image_to_string", return_value="corto")
    @patch("src.ocr.document_scanner.ImagePreprocessor.preprocess")
    def test_falls_back_to_easyocr_when_text_too_short(self, mock_pre, mock_tess, scanner):
        mock_pre.return_value = MagicMock()

        mock_reader = MagicMock()
        mock_reader.readtext.return_value = [
            (None, "12345678", 0.99),
            (None, "01/01/1990", 0.95),
        ]
        scanner._ocr_reader = mock_reader

        result = scanner.extract_dni_fields("fake_path.jpg")
        assert result["method_used"] == "easyocr"
