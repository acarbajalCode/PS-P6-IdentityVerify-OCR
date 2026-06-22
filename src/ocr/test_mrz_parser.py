from document_scanner import DocumentScanner
from mrz_parser import MRZParser


scanner = DocumentScanner()

text = scanner.extract_text(
    "tests/fixtures/dni/dni_back.jpeg"
)

print("\n===== OCR POSTERIOR =====\n")
print(text)

parser = MRZParser()

result = parser.parse(text)

print("\n===== DATOS MRZ =====\n")
print(result)