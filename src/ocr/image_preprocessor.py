import cv2
import numpy as np


class ImagePreprocessor:
    """
    Preprocesa imágenes de documentos de identidad para mejorar la precisión del OCR.
    Pipeline: resize → grayscale → deskew → denoise → binarize (Otsu).
    """

    TARGET_WIDTH = 1200   # Ancho óptimo para Tesseract

    def preprocess(self, image_path: str) -> np.ndarray:
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"No se pudo cargar la imagen: {image_path}")

        img = self._resize(img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = self._deskew(gray)
        gray = self._denoise(gray)
        binary = self._binarize(gray)
        return binary

    def _resize(self, img: np.ndarray) -> np.ndarray:
        h, w = img.shape[:2]
        if w < self.TARGET_WIDTH:
            scale = self.TARGET_WIDTH / w
            img = cv2.resize(img, None, fx=scale, fy=scale,
                             interpolation=cv2.INTER_CUBIC)
        return img

    def _deskew(self, gray: np.ndarray) -> np.ndarray:
        coords = np.column_stack(np.where(gray < 128))
        if len(coords) == 0:
            return gray
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = 90 + angle
        if abs(angle) < 0.5:
            return gray
        h, w = gray.shape
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        return cv2.warpAffine(gray, M, (w, h),
                              flags=cv2.INTER_CUBIC,
                              borderMode=cv2.BORDER_REPLICATE)

    def _denoise(self, gray: np.ndarray) -> np.ndarray:
        return cv2.fastNlMeansDenoising(gray, h=10, templateWindowSize=7,
                                        searchWindowSize=21)

    def _binarize(self, gray: np.ndarray) -> np.ndarray:
        _, binary = cv2.threshold(gray, 0, 255,
                                  cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return binary
