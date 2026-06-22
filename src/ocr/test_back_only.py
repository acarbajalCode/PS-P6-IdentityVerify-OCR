from document_scanner import DocumentScanner
from mrz_parser import MRZParser


scanner = DocumentScanner()

back_text = scanner.extract_text(
    "tests/fixtures/dni/dni_back.jpeg"
)

print("\n================ BACK RAW ================\n")
print(back_text)

parser = MRZParser()

result = parser.parse(back_text)

print("\n================ MRZ RESULT ================\n")
print(result)