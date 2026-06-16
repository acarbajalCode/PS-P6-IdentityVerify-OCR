# Threat Model — STRIDE — UQ·VerifyID

Fecha: 2026-06-16 | Metodología: STRIDE | Autor: G6 UQ·VerifyID

## Activos a proteger

| Activo | Sensibilidad | Propietario |
|---|---|---|
| Imagen del DNI del usuario | CRÍTICA | Usuario |
| Selfie del usuario | ALTA | Usuario |
| Datos extraídos por OCR (nombre, DNI, fechas) | CRÍTICA | Usuario |
| JWT de sesión | ALTA | Sistema |
| SECRET_KEY del servidor | CRÍTICA | UQ AI SOLUTION |
| Resultados de verificación | MEDIA | UQ AI SOLUTION |

---

## Análisis STRIDE completo

### S — Spoofing (Suplantación de identidad)

| ID | Amenaza | Componente | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|---|
| S1 | Atacante usa foto impresa para engañar al sistema de reconocimiento facial | Face Matcher | Alta | Crítico | Liveness detection (Laplacian + variación de frames) |
| S2 | Atacante usa máscara 3D para pasar el liveness | Liveness Detector | Baja | Crítico | Blink detection + Optical Flow (S3) |
| S3 | Atacante roba JWT válido y lo usa desde otra IP | Auth JWT | Media | Alto | Expiración 15 min; considerar IP binding en S6 |
| S4 | Atacante usa foto de pantalla (teléfono con foto de otra persona) | Liveness Detector | Alta | Alto | Análisis Laplacian detecta patrones de pantalla LCD |

### T — Tampering (Manipulación de datos)

| ID | Amenaza | Componente | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|---|
| T1 | Atacante edita imagen del DNI con Photoshop para cambiar nombre o número | OCR + Fraud | Alta | Crítico | ELA (Error Level Analysis) detecta zonas editadas |
| T2 | Atacante manipula la petición HTTP entre selfie y servidor (MITM) | API | Media | Alto | TLS 1.3 obligatorio; certificado válido en Azure |
| T3 | Atacante modifica la respuesta JSON en tránsito para cambiar `approved:false` a `true` | API response | Baja | Crítico | TLS + firma de respuesta (planificado S6) |
| T4 | Path traversal: atacante sube un archivo con nombre `../../etc/passwd` | File Upload | Media | Alto | Nombre de archivo ignorado; se genera UUID aleatorio |

### R — Repudiation (Repudio)

| ID | Amenaza | Componente | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|---|
| R1 | Usuario niega haber realizado una verificación | API | Media | Medio | Registro en BD con `request_id`, timestamp, IP, user-agent |
| R2 | Operador modifica logs de auditoría para encubrir acceso indebido | BD | Baja | Alto | Azure Monitor con logs inmutables (write-once) |

### I — Information Disclosure (Divulgación de información)

| ID | Amenaza | Componente | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|---|
| I1 | Imagen del DNI queda en disco del servidor después del proceso | File System | Alta | Crítico | Bloque `finally` borra archivos temporales siempre |
| I2 | Stack trace del servidor expuesto en respuesta de error | API | Media | Medio | `debug=False` en producción; respuestas genéricas de error |
| I3 | Datos del OCR almacenados en logs sin cifrar | Logs | Media | Alto | Logs sin campos sensibles; Azure Monitor con RBAC |
| I4 | SECRET_KEY expuesta en código fuente o variable de entorno no cifrada | Auth | Baja | Crítico | Azure Key Vault; `.env` en `.gitignore` |

### D — Denial of Service (Denegación de servicio)

| ID | Amenaza | Componente | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|---|
| D1 | Atacante sube imágenes de 100 MB repetidamente para agotar disco/memoria | File Upload | Alta | Alto | Límite 5 MB por archivo; validación antes de guardar |
| D2 | Atacante envía 1000 solicitudes por minuto agotando CPU (DeepFace es costoso) | API | Media | Alto | Rate limiting: 5 req/min/IP; Azure autoscaling |
| D3 | DeepFace carga modelos pesados en cada request agotando RAM | Face Matcher | Media | Medio | Instancia singleton por módulo; modelos cargados una vez |

### E — Elevation of Privilege (Escalada de privilegios)

| ID | Amenaza | Componente | Probabilidad | Impacto | Mitigación |
|---|---|---|---|---|---|
| E1 | Atacante modifica payload del JWT para cambiar su rol (ej: user→admin) | Auth JWT | Media | Crítico | Verificación de firma HS256; clave de 32 bytes mínimo |
| E2 | Atacante accede a endpoint `/admin/sesiones` sin ser admin | API RBAC | Baja | Alto | `require_role('admin')` en decorador (implementar en S5) |
| E3 | Código malicioso inyectado en nombre de archivo procesado como shell command | File System | Baja | Crítico | Nombre de archivo nunca se usa; UUID aleatorio siempre |

---

## Resumen de riesgos por prioridad

| Prioridad | Amenazas | Estado |
|---|---|---|
| 🔴 Crítico | S1, T1, I1, I4, E1 | Mitigado en diseño base |
| 🟠 Alto | S3, T2, D1, D2, E2 | Mitigado en S3–S6 |
| 🟡 Medio | R1, I2, I3, D3, S4 | Mitigado en S5–S7 |
| 🟢 Bajo | S2, T3, R2, T4, E3 | Aceptado o mitigado parcialmente |
