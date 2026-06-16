import io
import numpy as np
from PIL import Image


class ELAAnalyzer:
    """
    Error Level Analysis (ELA).

    Las imágenes JPEG pierden calidad en cada re-compresión. Si una zona
    de la imagen fue editada y guardada por separado, su nivel de error
    diferirá del resto al re-comprimir. ELA amplifica esa diferencia.

    Referencia: Krawetz, N. (2007). A picture's worth. Hacker Factor Solutions.
    """

    RECOMPRESS_QUALITY = 90   # Calidad de la re-compresión de referencia
    AMPLIFY_SCALE      = 15   # Factor de amplificación visual

    def compute(self, image_path: str) -> dict:
        """
        Calcula el score ELA de una imagen.

        Returns:
            dict con: mean_score, max_score, std_score, interpretation
        """
        original = Image.open(image_path).convert("RGB")

        # Re-comprimir a calidad controlada
        buffer = io.BytesIO()
        original.save(buffer, format="JPEG", quality=self.RECOMPRESS_QUALITY)
        buffer.seek(0)
        recompressed = Image.open(buffer).convert("RGB")

        # Diferencia amplificada (canal por canal)
        orig_arr  = np.array(original,     dtype=np.int16)
        recomp_arr = np.array(recompressed, dtype=np.int16)
        ela_arr   = np.abs(orig_arr - recomp_arr) * self.AMPLIFY_SCALE
        ela_arr   = np.clip(ela_arr, 0, 255).astype(np.uint8)

        mean_score = float(np.mean(ela_arr))
        max_score  = float(np.max(ela_arr))
        std_score  = float(np.std(ela_arr))

        return {
            "mean_score":    round(mean_score, 4),
            "max_score":     round(max_score, 4),
            "std_score":     round(std_score, 4),
            "interpretation": self._interpret(mean_score),
        }

    def _interpret(self, mean_score: float) -> str:
        if mean_score < 3.0:
            return "authentic"
        if mean_score < 8.0:
            return "suspicious — manual review recommended"
        return "likely_tampered"

    def generate_ela_image(self, image_path: str, output_path: str) -> None:
        """Guarda la imagen ELA amplificada para inspección visual."""
        original = Image.open(image_path).convert("RGB")
        buffer   = io.BytesIO()
        original.save(buffer, format="JPEG", quality=self.RECOMPRESS_QUALITY)
        buffer.seek(0)
        recompressed = Image.open(buffer).convert("RGB")

        orig_arr   = np.array(original,      dtype=np.int16)
        recomp_arr = np.array(recompressed,  dtype=np.int16)
        ela_arr    = np.abs(orig_arr - recomp_arr) * self.AMPLIFY_SCALE
        ela_arr    = np.clip(ela_arr, 0, 255).astype(np.uint8)

        Image.fromarray(ela_arr).save(output_path)
