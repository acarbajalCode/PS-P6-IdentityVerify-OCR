# Semana 7 — PenTest por G5 + Hardening Final

**Rama:** `feature/s7-pentest-hardening` → PR hacia `main`

## Entregables
- [ ] `PenTest_Report_G5.md` — recibido de G5 (UQ·AuditAI)
- [ ] `Hardening_Response.md` — correcciones implementadas por G6
- [ ] OWASP ZAP scan completado contra la URL pública
- [ ] Checklist OWASP API Security Top 10 completado al ≥80%

## PenTest_Report_G5.md (llenar con reporte de G5)

| # | Vulnerabilidad | Severidad | CVSS | Descripción | Estado |
|---|---|---|---|---|---|
| 1 | | | | | ⬜ Pendiente |
| 2 | | | | | ⬜ Pendiente |
| 3 | | | | | ⬜ Pendiente |

## Hardening_Response.md (llenar por G6)

| Vulnerabilidad encontrada | Corrección aplicada | Commit |
|---|---|---|
| | | |

## Vectores de ataque a probar

```bash
# 1. Path traversal en upload de imagen
curl -X POST .../verify-identity \
  -F "document=@../../../../etc/passwd"

# 2. Imagen gigante (DoS)
dd if=/dev/zero bs=1M count=100 | curl -X POST .../verify-identity -F "document=@-"

# 3. Archivo no-imagen disfrazado de JPG
echo "SHELL SCRIPT" > malicious.jpg
curl -X POST .../verify-identity -F "document=@malicious.jpg"

# 4. JWT manipulado (cambiar rol)
# Decodificar JWT, cambiar payload, re-encodear sin firma
```
