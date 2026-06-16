# STRIDE Threat Model — Semana 1
## UQ·VerifyID — Verificación de Identidad con OCR y Reconocimiento Facial

**Equipo:** G6 — UQ·VerifyID  
**Fecha:** _______________  
**Versión:** 1.0

---

## Activos del sistema (completar en clase)

| Activo | Descripción | Nivel de sensibilidad |
|---|---|---|
| Imagen DNI | | |
| Selfie del usuario | | |
| Datos OCR extraídos | | |
| Token JWT | | |
| SECRET_KEY | | |

---

## Análisis STRIDE (completar con el equipo)

| Categoría | Pregunta guía | Amenaza identificada | Componente afectado | Mitigación propuesta |
|---|---|---|---|---|
| **S**poofing | ¿Cómo puede un atacante hacerse pasar por otro usuario? | | | |
| **T**ampering | ¿Cómo puede un atacante modificar el DNI antes de enviarlo? | | | |
| **R**epudiation | ¿Puede un usuario negar haber hecho una verificación? | | | |
| **I**nfo Disclosure | ¿Dónde pueden quedar expuestas las imágenes del DNI? | | | |
| **D**enial of Service | ¿Cómo puede un atacante saturar el sistema de verificación? | | | |
| **E**levation of Privilege | ¿Puede alguien acceder a resultados de otros usuarios? | | | |

---

## Diagrama de flujo de datos (completar)

```
[Usuario] → [Subir DNI + Selfie] → [API FastAPI] → [OCR] → [Face Match] → [Resultado]
                                        ↓
                                   [¿Dónde hay amenazas?]
```

Marca con ⚠️ los puntos de amenaza en el diagrama.

---

## Reflexión del equipo

¿Cuál es la amenaza más crítica que identificaron y por qué?

_____________________________________________________________
_____________________________________________________________
_____________________________________________________________

Ver solución completa en: `docs/threat-model.md`
