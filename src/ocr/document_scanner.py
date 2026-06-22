import pytesseract

from src.ocr.image_preprocessor import ImagePreprocessor


class DocumentScanner:

    def __init__(self):
        self.preprocessor = ImagePreprocessor()

    def extract_text(self, image_path: str) -> str:
        """
        Extrae texto completo utilizando Tesseract.
        """

        processed_image = self.preprocessor.preprocess(
            image_path
        )

        extracted_text = pytesseract.image_to_string(
            processed_image,
            lang="spa"
        )

        return extracted_text.strip()