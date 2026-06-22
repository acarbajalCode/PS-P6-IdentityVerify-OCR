from document_scanner import DocumentScanner
from mrz_parser import MRZParser
from dni_parser import DNIParser
from identity_validator import IdentityValidator

print(">>> EJECUTANDO VERSION NUEVA FINAL <<<")

scanner = DocumentScanner()

# 🔴 FRONTAL
front_text = scanner.extract_text(
    "tests/fixtures/dni/dni_front.jpeg"
)

# 🔴 POSTERIOR
back_text = scanner.extract_text(
    "tests/fixtures/dni/dni_back.jpeg"
)

print("\n================ FRONT RAW ================\n")
print(front_text)

print("\n================ BACK RAW ================\n")
print(back_text)

# =========================
# PARSERS
# =========================
mrz_data = MRZParser().parse(back_text)
ocr_data = DNIParser().parse(front_text)

# 🔥 FIX CRÍTICO: pasar texto completo al validador
ocr_data["raw_text"] = front_text

print("\n================ MRZ PARSED ================\n")
print(mrz_data)

print("\n================ OCR PARSED ================\n")
print(ocr_data)

# =========================
# VALIDACIÓN FINAL
# =========================
validator = IdentityValidator()
result = validator.build_final_result(mrz_data, ocr_data)

print("\n================ FINAL RESULT ================\n")
print(result)