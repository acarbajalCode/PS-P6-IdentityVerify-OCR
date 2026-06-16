import piexif
from .ela_analyzer import ELAAnalyzer


SUSPICIOUS_SOFTWARE = {
    "photoshop", "gimp", "paint.net", "lightroom",
    "affinity", "pixelmator", "canva", "inkscape",
}


class FraudDetector:
    """
    Detecta documentos de identidad falsificados combinando:
    1. ELA (Error Level Analysis) — zonas editadas con Photoshop/GIMP.
    2. Metadatos EXIF — software de edición en cabecera del archivo.
    3. Reglas heurísticas — umbral configurable por despliegue.

    En S5 se agrega un clasificador XGBoost entrenado con dataset sintético.
    """

    def __init__(self, ela_threshold: float = 8.0):
        self._ela = ELAAnalyzer()
        self._ela_threshold = ela_threshold

    # ── API principal ────────────────────────────────────────────────────────

    def predict(self, image_path: str) -> dict:
        """
        Predicción consolidada de fraude para un documento.

        Returns:
            dict con: is_fraud, fraud_score (0–1), ela, exif, signals
        """
        ela_result  = self._ela.compute(image_path)
        exif_result = self._analyze_exif(image_path)

        signals = []
        score   = 0.0

        if ela_result["mean_score"] > self._ela_threshold:
            signals.append(f"ELA score {ela_result['mean_score']:.2f} > {self._ela_threshold}")
            score += ela_result["mean_score"] / 20.0

        if exif_result["is_suspicious"]:
            signals.append(f"Editing software detected: {exif_result['software']}")
            score += 0.4

        score    = round(min(score, 1.0), 4)
        is_fraud = bool(signals)

        return {
            "is_fraud":    is_fraud,
            "fraud_score": score,
            "ela":         ela_result,
            "exif":        exif_result,
            "signals":     signals,
        }

    # ── Análisis EXIF ────────────────────────────────────────────────────────

    def _analyze_exif(self, image_path: str) -> dict:
        try:
            exif_data = piexif.load(image_path)
            raw_software = exif_data.get("0th", {}).get(piexif.ImageIFD.Software, b"")
            software = raw_software.decode("utf-8", errors="ignore").lower().strip()
            is_suspicious = any(s in software for s in SUSPICIOUS_SOFTWARE)
            return {"software": software or "none", "is_suspicious": is_suspicious}
        except Exception:
            return {"software": "unreadable", "is_suspicious": False}
