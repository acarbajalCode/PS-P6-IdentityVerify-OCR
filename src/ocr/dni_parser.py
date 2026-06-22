import re


class DNIParser:

    def clean(self, text: str):
        return re.sub(r"[^A-ZÁÉÍÓÚÑ 0-9\n]", " ", text.upper())

    def parse(self, text: str):

        text = self.clean(text)

        result = {
            "dni_number": None,
            "apellido_paterno": None,
            "apellido_materno": None,
            "nombres": None,
            "fecha_emision": None,
            "dates": [],
            "raw_text": text
        }

        # ================= DNI =================
        dni_match = re.search(r"\b\d{8}\b", text)
        if dni_match:
            result["dni_number"] = dni_match.group(0)

        # ================= NOMBRES =================
        name_match = re.search(r"PRENOMBRES\s*\n([A-ZÁÉÍÓÚÑ ]+)", text)
        if name_match:
            result["nombres"] = name_match.group(1).strip()

        # ========== 2.0 FORMATO ==========
        paterno = re.search(r"PRIMER APELLIDO\s*\n([A-ZÁÉÍÓÚÑ ]+)", text)
        materno = re.search(r"SEGUNDO APELLIDO\s*\n([A-ZÁÉÍÓÚÑ ]+)", text)

        if paterno:
            result["apellido_paterno"] = paterno.group(1).strip()

        if materno:
            val = materno.group(1).strip()
            if val not in ["UN", "E", ""]:
                result["apellido_materno"] = val

        # ========== 3.0 FORMATO ==========
        apellidos = re.search(r"APELLIDOS\s*\n([A-ZÁÉÍÓÚÑ ]+)", text)
        if apellidos:
            parts = apellidos.group(1).split()

            if len(parts) >= 2:
                result["apellido_paterno"] = parts[0]
                result["apellido_materno"] = " ".join(parts[1:])
            elif len(parts) == 1:
                result["apellido_paterno"] = parts[0]

        # ========== FALLBACK INTELIGENTE ==========
        if not result["apellido_materno"]:
            fallback = re.findall(r"\n([A-ZÁÉÍÓÚÑ]{3,})\n", text)

            # evita tomar nombres
            blacklist = {"PERÚ", "REGISTRO", "IDENTIDAD"}

            for f in fallback:
                if f not in blacklist and f != result["apellido_paterno"]:
                    result["apellido_materno"] = f
                    break

        # ================= FECHAS =================
        result["dates"] = re.findall(r"\d{2}[\/\s]\d{2}[\/\s]\d{4}", text)

        return result