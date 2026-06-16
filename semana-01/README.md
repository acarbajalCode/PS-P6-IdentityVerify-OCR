# Semana 1 — Setup + STRIDE Threat Modeling

**Rama:** `feature/s1-setup-stride` → PR hacia `main`

## Entregables
- [ ] Repositorio configurado con estructura completa
- [ ] `requirements.txt` instalado y verificado
- [ ] Diagrama de arquitectura (Mermaid o draw.io)
- [ ] `STRIDE_ThreatModel.md` — 6 amenazas identificadas para el pipeline OCR+Face
- [ ] Dataset sintético: 20 imágenes DNI ficticias en `tests/fixtures/`
- [ ] Entorno Python 3.11 documentado

## STRIDE_ThreatModel.md (completar)

| Categoría STRIDE | Amenaza específica | Componente | Mitigación propuesta |
|---|---|---|---|
| Spoofing | | | |
| Tampering | | | |
| Repudiation | | | |
| Info Disclosure | | | |
| Denial of Service | | | |
| Elevation of Privilege | | | |

## Puntos de verificación
- `python -c "import fastapi, cv2, pytesseract; print('OK')"` — debe imprimir OK
- `tesseract --version` — debe mostrar Tesseract 5.x
