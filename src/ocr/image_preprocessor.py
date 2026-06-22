import cv2
from pathlib import Path


class ImagePreprocessor:
    """
    Responsable del preprocesamiento de imágenes
    antes de ser enviadas al motor OCR.
    """

    ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}

    def validate_image(self, image_path: str) -> bool:
        """
        Valida existencia y extensión permitida.
        """

        path = Path(image_path)

        if not path.exists():
            raise FileNotFoundError(
                f"No existe el archivo: {image_path}"
            )

        if path.suffix.lower() not in self.ALLOWED_EXTENSIONS:
            raise ValueError(
                "Formato no permitido. Use JPG, JPEG o PNG."
            )

        return True

    def preprocess(self, image_path: str):
        """
        Aplica preprocesamiento básico para OCR.
        """

        self.validate_image(image_path)

        image = cv2.imread(image_path)

        if image is None:
            raise ValueError(
                "No fue posible leer la imagen."
            )

        # Escala de grises
        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )
        gray = cv2.resize(
            gray,
            None,
            fx=2,
            fy=2,
            interpolation=cv2.INTER_CUBIC
        )

        # Reducción de ruido
        blurred = cv2.GaussianBlur(
            gray,
            (5, 5),
            0
        )

        # Binarización
        _, threshold = cv2.threshold(
            blurred,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        return threshold