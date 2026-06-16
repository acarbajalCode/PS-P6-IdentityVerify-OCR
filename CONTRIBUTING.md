# Guía de Contribución — PS-P6 UQ·VerifyID

## Flujo de trabajo Git

```bash
# 1. Fork en GitHub → clonar tu fork
git clone https://github.com/TU-USUARIO/PS-P6-IdentityVerify-OCR.git

# 2. Crear rama para la semana
git checkout -b feature/s1-setup-stride

# 3. Desarrollar → commit frecuente
git add src/ocr/document_scanner.py
git commit -m "feat(ocr): agregar preprocessing con OpenCV"

# 4. Push a tu fork
git push origin feature/s1-setup-stride

# 5. Abrir PR en GitHub → solicitar revisión del docente
```

## Regla crítica de seguridad

**NUNCA subir imágenes reales de DNI al repositorio.**
Usa siempre imágenes sintéticas en `tests/fixtures/synthetic_*.jpg`.

## Convención de commits

- `feat(módulo):` nueva funcionalidad
- `fix(módulo):` corrección de bug
- `test(módulo):` agregar o mejorar tests
- `security(módulo):` mejora de seguridad
- `docs:` documentación

## Checklist antes de cada PR

- [ ] `bandit -r src/` no reporta vulnerabilidades HIGH
- [ ] `pytest tests/` pasa al 100%
- [ ] No hay credenciales ni imágenes reales en el commit
- [ ] El `semana-XX/README.md` está actualizado con los entregables
