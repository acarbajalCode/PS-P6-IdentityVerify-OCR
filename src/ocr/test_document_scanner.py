from document_scanner import DocumentScanner


scanner = DocumentScanner()

text = scanner.extract_text(
    "tests/fixtures/dni/dni_test_004.png"
)

print("\n===== TEXTO EXTRAÍDO =====\n")
print(text)