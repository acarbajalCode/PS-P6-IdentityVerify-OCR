import re
from datetime import datetime


def clean_text(text: str) -> str:
    """
    Normaliza espacios y saltos de línea.
    """

    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def extract_dates(text: str):
    """
    Busca fechas con formato:
    18 05 1996
    18/05/1996
    18-05-1996
    """

    pattern = r"\b\d{2}[\/\-\s]\d{2}[\/\-\s]\d{4}\b"

    return re.findall(pattern, text)


def calculate_age(date_str: str):
    """
    Calcula edad a partir de una fecha.
    """

    try:

        birth_date = datetime.strptime(date_str, "%d/%m/%Y")

        today = datetime.today()

        age = today.year - birth_date.year

        if (
            (today.month, today.day)
            <
            (birth_date.month, birth_date.day)
        ):
            age -= 1

        return age

    except Exception:
        return None


def is_adult(age: int):

    if age is None:
        return False

    return age >= 18


def is_document_valid(expiration_date: str):

    try:

        if not expiration_date:
            return False

        if "NO CADUCA" in expiration_date.upper():
            return True

        expiration = datetime.strptime(
            expiration_date,
            "%d/%m/%Y"
        )

        return expiration.date() >= datetime.today().date()

    except Exception:
        return False