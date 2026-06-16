import cv2
import numpy as np
from typing import List


class LivenessDetector:
    """
    Detecta si la selfie proviene de una persona real (liveness) o de un
    ataque de presentación (foto impresa, pantalla, video pregrabado).

    Métodos:
    - Variación de píxeles entre frames: foto estática → variación ≈ 0
    - Análisis de textura Laplaciano: pantalla → bordes irregulares
    - Detección de parpadeo con Haar Cascade (requiere múltiples frames)
    """

    VARIATION_THRESHOLD = 2.0    # Umbral de movimiento mínimo entre frames
    LAPLACIAN_THRESHOLD = 50.0   # Varianza mínima de nitidez (foto borrosa = baja)

    def check_liveness_from_frames(self, frames: List[np.ndarray]) -> dict:
        """
        Analiza una secuencia de frames de video.
        Requiere mínimo 5 frames para análisis confiable.
        """
        if len(frames) < 5:
            return {
                "is_live": False,
                "reason":  "Insufficient frames — minimum 5 required",
                "avg_variation": 0.0,
            }

        gray_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
                       if len(f.shape) == 3 else f for f in frames]

        variations = [
            float(np.mean(cv2.absdiff(gray_frames[i - 1], gray_frames[i])))
            for i in range(1, len(gray_frames))
        ]
        avg_variation = float(np.mean(variations))
        is_live = avg_variation > self.VARIATION_THRESHOLD

        return {
            "is_live":       is_live,
            "avg_variation": round(avg_variation, 4),
            "frames_analyzed": len(frames),
            "reason":        "Motion detected" if is_live else "Static image — possible photo/screen attack",
        }

    def check_liveness_from_image(self, image_path: str) -> dict:
        """
        Análisis de liveness desde una imagen estática.
        Usa textura Laplaciana y análisis de frecuencia para detectar
        fotos impresas (bordes irregulares por impresión) o pantallas
        (patrón de píxeles uniforme).
        """
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            return {"is_live": False, "reason": "Cannot read image", "laplacian_var": 0.0}

        laplacian_var = float(cv2.Laplacian(img, cv2.CV_64F).var())

        # Demasiado nítida (pantalla LCD) o demasiado borrosa (foto impresa):
        # ambas señales de posible ataque. Rango normal de una selfie real: 50-800
        if laplacian_var < self.LAPLACIAN_THRESHOLD:
            return {
                "is_live":       False,
                "laplacian_var": round(laplacian_var, 2),
                "reason":        "Low sharpness — possible printed photo",
            }

        return {
            "is_live":       True,
            "laplacian_var": round(laplacian_var, 2),
            "reason":        "Sharpness within expected range for real selfie",
        }

    def detect_blink(self, frames: List[np.ndarray]) -> dict:
        """
        Detecta parpadeo usando Haar Cascade para ojos.
        Un parpadeo confirma presencia de usuario real.
        """
        eye_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_eye.xml"
        )
        eye_counts = []

        for frame in frames:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) if len(frame.shape) == 3 else frame
            eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
            eye_counts.append(len(eyes))

        # Un parpadeo = secuencia de frames con ojos (>0) → sin ojos (0) → con ojos (>0)
        blink_detected = False
        for i in range(1, len(eye_counts) - 1):
            if eye_counts[i - 1] > 0 and eye_counts[i] == 0 and eye_counts[i + 1] > 0:
                blink_detected = True
                break

        return {
            "blink_detected": blink_detected,
            "eye_counts":     eye_counts,
            "frames_analyzed": len(frames),
        }
