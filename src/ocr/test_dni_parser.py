from document_scanner import DocumentScanner


scanner = DocumentScanner()

print("\n==============================")
print("OCR DNI - CARA FRONTAL")
print("==============================\n")

front_text = scanner.extract_text(
    "tests/fixtures/dni/dni_front.jpeg"
)

print(front_text)

print("\n==============================")
print("OCR DNI - CARA POSTERIOR")
print("==============================\n")

back_text = scanner.extract_text(
    "tests/fixtures/dni/dni_back.jpeg"
)

print(back_text)