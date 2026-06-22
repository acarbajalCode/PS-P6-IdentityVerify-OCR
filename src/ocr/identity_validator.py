from datetime import datetime


class IdentityValidator:

    def calculate_age(self, birth_date: str):

        try:
            if not birth_date:
                return None

            day, month, year = map(int, birth_date.split("/"))
            birth = datetime(year, month, day)

            today = datetime.today()

            age = today.year - birth.year

            if (today.month, today.day) < (birth.month, birth.day):
                age -= 1

            return age

        except:
            return None

    def is_adult(self, birth_date: str):
        age = self.calculate_age(birth_date)
        return age >= 18 if age is not None else False

    # ================= FIX DEFINITIVO =================
    def is_document_valid(self, expiry_date: str, ocr_data: dict = None):

        try:
            ocr_text = str(ocr_data.get("raw_text", "")).upper() if ocr_data else ""

            # 🔥 PRIORIDAD ABSOLUTA
            if "NO CADUCA" in ocr_text:
                return True

            if not expiry_date:
                return False

            day, month, year = map(int, expiry_date.split("/"))
            expiry = datetime(year, month, day)

            return expiry >= datetime.today()

        except:
            return False

    def normalize_date(self, date_str: str):

        if not date_str:
            return None

        date_str = date_str.replace(" ", "/").strip()
        parts = date_str.split("/")

        if len(parts) != 3:
            return None

        return f"{parts[0]}/{parts[1]}/{parts[2]}"

    def consolidate(self, mrz_data: dict, ocr_data: dict):

        ocr_text = str(ocr_data.get("raw_text", "")).upper()

        nombres = ocr_data.get("nombres") or mrz_data.get("nombres")

        # limpiar MRZ corrupto
        if nombres:
            nombres = nombres.replace("]", "A")

        apellido_paterno = mrz_data.get("apellido_paterno") or ocr_data.get("apellido_paterno")
        apellido_materno = ocr_data.get("apellido_materno") or mrz_data.get("apellido_materno")

        # ================= FECHAS =================
        fecha_nacimiento = mrz_data.get("fecha_nacimiento")
        fecha_emision = self.normalize_date(ocr_data.get("fecha_emision"))

        # 🔥 CLAVE: NO CADUCA SOLO DESDE OCR
        if "NO CADUCA" in ocr_text:
            fecha_vencimiento = "NO CADUCA"
        else:
            fecha_vencimiento = mrz_data.get("fecha_vencimiento")

        return {
            "dni_number": mrz_data.get("dni_number"),
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno,
            "nombres": nombres,
            "fecha_nacimiento": fecha_nacimiento,
            "fecha_emision": fecha_emision,
            "fecha_vencimiento": fecha_vencimiento
        }

    def build_final_result(self, mrz_data: dict, ocr_data: dict):

        consolidated = self.consolidate(mrz_data, ocr_data)

        return {
            **consolidated,
            "edad": self.calculate_age(consolidated["fecha_nacimiento"]),
            "mayor_de_edad": self.is_adult(consolidated["fecha_nacimiento"]),
            "documento_vigente": self.is_document_valid(
                consolidated["fecha_vencimiento"],
                ocr_data
            )
        }