import re
import pytesseract
import easyocr
from .image_preprocessor import ImagePreprocessor


class DNIScanner:
    """
    Pipeline OCR para extracción segura de datos del DNI peruano.
    Combina Tesseract 5 (primary) + EasyOCR (fallback) para máxima precisión.
    Soporta DNI peruano: 8 dígitos, MRZ, nombres en mayúsculas.
    """

    TESSERACT_CONFIG = "--psm 6 -l spa"
    MIN_TEXT_LENGTH = 20   # Si Tesseract extrae menos caracteres, activa EasyOCR

    def __init__(self):
        self._preprocessor = ImagePreprocessor()
        self._ocr_reader = None   # Lazy init — EasyOCR tarda en cargar

    @property
    def _easyocr(self):
        if self._ocr_reader is None:
            self._ocr_reader = easyocr.Reader(["es", "en"], gpu=False, verbose=False)
        return self._ocr_reader

    def extract_dni_fields(self, image_path: str) -> dict:
        """
        Extrae los campos del DNI peruano desde una imagen.

        Returns:
            dict con: dni_number, nombre, apellido_paterno, apellido_materno,
                      fecha_nac, fecha_venc, valid, raw_text, method_used
        """
        processed = self._preprocessor.preprocess(image_path)
        text = pytesseract.image_to_string(processed, config=self.TESSERACT_CONFIG)

        if len(text.strip()) < self.MIN_TEXT_LENGTH:
            results = self._easyocr.readtext(image_path, detail=0)
            text = " ".join(results)
            method = "easyocr"
        else:
            method = "tesseract"

        fields = self._parse_fields(text)
        fields["raw_text"] = text.strip()
        fields["method_used"] = method
        fields["valid"] = bool(fields["dni_number"] and fields["fecha_nac"])
        return fields

    def _parse_fields(self, text: str) -> dict:
        dni_number = self._extract_dni_number(text)
        dates = re.findall(r"\b(\d{2}[/\-\.]\d{2}[/\-\.]\d{4})\b", text)
        names = self._extract_names(text)

        return {
            "dni_number":       dni_number,
            "apellido_paterno": names.get("apellido_paterno"),
            "apellido_materno": names.get("apellido_materno"),
            "nombre":           names.get("nombre"),
            "fecha_nac":        dates[0] if len(dates) > 0 else None,
            "fecha_venc":       dates[1] if len(dates) > 1 else None,
        }

    def _extract_dni_number(self, text: str) -> str | None:
        # Prioriza bloques de exactamente 8 dígitos rodeados de espacios
        matches = re.findall(r"(?<!\d)(\d{8})(?!\d)", text)
        return matches[0] if matches else None

    def _extract_names(self, text: str) -> dict:
        # Los apellidos y nombres en el DNI peruano están en mayúsculas
        lines = [l.strip() for l in text.splitlines() if l.strip().isupper()
                 and len(l.strip()) > 3]
        return {
            "apellido_paterno": lines[0] if len(lines) > 0 else None,
            "apellido_materno": lines[1] if len(lines) > 1 else None,
            "nombre":           lines[2] if len(lines) > 2 else None,
        }
