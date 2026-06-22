import re
from datetime import datetime


class MRZParser:

    def extract_mrz_lines(self, text: str):
        lines = []

        for line in text.splitlines():
            line = line.strip()
            if "<" in line and len(line) > 20:
                lines.append(line)

        return lines

    def parse(self, text: str):

        lines = self.extract_mrz_lines(text)

        result = {
            "dni_number": None,
            "fecha_nacimiento": None,
            "fecha_vencimiento": None,
            "apellido_paterno": None,
            "nombres": None
        }

        if len(lines) < 3:
            return result

        line1, line2, line3 = lines[-3:]

        # ================= DNI =================
        dni_match = re.search(r"PER(\d{8})", line1)
        if dni_match:
            result["dni_number"] = dni_match.group(1)

        # ========== FECHA NACIMIENTO ==========
        birth_match = re.search(r"(\d{6})", line2)
        if birth_match:
            birth = birth_match.group(1)

            dd = birth[4:6]
            mm = birth[2:4]
            yy = int(birth[0:2])

            current_year = int(str(datetime.today().year)[2:4])

            year = 2000 + yy if yy <= current_year else 1900 + yy

            result["fecha_nacimiento"] = f"{dd}/{mm}/{year}"

        # ========== FECHA VENCIMIENTO ==========
        expiry_match = re.search(r"\d{6}[A-Z0-9](\d{6})", line2)
        if expiry_match:
            exp = expiry_match.group(1)

            dd = exp[4:6]
            mm = exp[2:4]
            yy = int(exp[0:2])

            # MRZ siempre futuro (pero puede ser basura)
            result["fecha_vencimiento"] = f"{dd}/{mm}/{2000 + yy}"

        # ========== NOMBRES MRZ ==========
        if "<<" in line3:
            parts = line3.split("<<")
            result["apellido_paterno"] = parts[0].replace("<", "").strip()
            if len(parts) > 1:
                result["nombres"] = parts[1].replace("<", " ").strip()

        return result