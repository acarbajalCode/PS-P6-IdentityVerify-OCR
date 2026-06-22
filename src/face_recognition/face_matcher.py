from deepface import DeepFace


class FaceMatcher:

    def __init__(self, model_name="ArcFace", distance_metric="cosine"):
        self.model_name = model_name
        self.distance_metric = distance_metric

    def compare_faces(self, img1_path: str, img2_path: str):
        try:
            result = DeepFace.verify(
                img1_path=img1_path,
                img2_path=img2_path,
                model_name=self.model_name,
                distance_metric=self.distance_metric,
                enforce_detection=False
            )

            return {
                "match": result.get("verified"),
                "distance": result.get("distance"),
                "threshold": result.get("threshold"),
                "model": self.model_name
            }

        except Exception as e:
            return {
                "error": str(e),
                "match": False
            }