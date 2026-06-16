import numpy as np
from deepface import DeepFace


class FaceMatcher:
    """
    Comparación facial segura usando ensemble de modelos DeepFace.
    Combina VGG-Face, Facenet512 y ArcFace para mayor robustez ante
    variaciones de iluminación, ángulo y calidad de imagen.
    """

    SIMILARITY_THRESHOLD = 0.80
    MODELS = ["VGG-Face", "Facenet512", "ArcFace"]

    def verify_identity(self, selfie_path: str, document_photo_path: str) -> dict:
        """
        Compara la selfie del usuario con la foto extraída del documento.

        Returns:
            dict con: match, similarity, threshold, models_used, error (si aplica)
        """
        distances = []
        errors = []

        for model in self.MODELS:
            try:
                result = DeepFace.verify(
                    img1_path        = selfie_path,
                    img2_path        = document_photo_path,
                    model_name       = model,
                    distance_metric  = "cosine",
                    enforce_detection = True,
                    silent           = True,
                )
                distances.append(result["distance"])
            except Exception as e:
                errors.append(f"{model}: {str(e)}")

        if not distances:
            return {
                "match":       False,
                "similarity":  0.0,
                "threshold":   self.SIMILARITY_THRESHOLD,
                "models_used": 0,
                "error":       "; ".join(errors) or "No face detected in one or both images",
            }

        avg_distance = float(np.mean(distances))
        similarity   = round(1.0 - avg_distance, 4)

        return {
            "match":       similarity >= self.SIMILARITY_THRESHOLD,
            "similarity":  similarity,
            "threshold":   self.SIMILARITY_THRESHOLD,
            "models_used": len(distances),
            "error":       None,
        }

    def crop_face_from_document(self, document_image_path: str, output_path: str) -> bool:
        """
        Detecta y recorta la zona del rostro del documento para mejorar
        la comparación facial (elimina el fondo del DNI).
        """
        try:
            faces = DeepFace.extract_faces(
                img_path          = document_image_path,
                detector_backend  = "retinaface",
                enforce_detection = True,
            )
            if not faces:
                return False

            import cv2
            face_arr = (faces[0]["face"] * 255).astype("uint8")
            face_bgr = cv2.cvtColor(face_arr, cv2.COLOR_RGB2BGR)
            cv2.imwrite(output_path, face_bgr)
            return True
        except Exception:
            return False
