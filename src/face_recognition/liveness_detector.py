import cv2
import numpy as np


class LivenessDetector:

    def detect_blink(self, image_path: str):
        """
        Simulación básica de liveness.
        En producción: usar MediaPipe / EAR (Eye Aspect Ratio)
        """

        img = cv2.imread(image_path)

        if img is None:
            return {
                "live": False,
                "reason": "image_not_found"
            }

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        brightness = np.mean(gray)

        # heurística simple (demo)
        if brightness < 40:
            return {"live": False, "reason": "too_dark"}
        elif brightness > 220:
            return {"live": False, "reason": "too_bright"}

        return {
            "live": True,
            "reason": "face_likely_real"
        }