# S1_STRIDE_ThreatModel.md

# FaceDocVerify
## Modelo de Amenazas STRIDE

### Curso
Programación Segura

### Proyecto

**FaceDocVerify: A Multi-Modal Secure Identity Verification Framework Integrating Open-Source OCR and Deep Learning Facial Recognition with Real-Time Fraud Detection for Digital Onboarding Processes**

---

# 1. Objetivo

Identificar, analizar y mitigar las amenazas de seguridad presentes en la arquitectura inicial de FaceDocVerify mediante la metodología STRIDE, asegurando que el sistema implemente controles de seguridad desde las primeras etapas del desarrollo.

El análisis se enfoca en los componentes que formarán parte de la Exposición Parcial (Semana 4):

- API REST Segura
- Autenticación JWT
- OCR para extracción de datos del DNI
- Reconocimiento facial
- Validaciones de negocio
- Auditoría
- Almacenamiento temporal de imágenes

---

# 2. Alcance

El presente análisis cubre los siguientes componentes:

| Componente | Descripción |
|------------|------------|
| API REST | Recepción y procesamiento de solicitudes |
| JWT Authentication | Control de acceso a endpoints |
| OCR Service | Extracción de información del documento |
| Face Matching Service | Comparación entre selfie y foto del documento |
| Validation Service | Validación de edad y vigencia del documento |
| Audit Service | Registro de eventos y trazabilidad |
| Temporary Storage | Almacenamiento temporal de imágenes |

---

# 3. Arquitectura Analizada

La arquitectura evaluada corresponde a la definida en:

- S1_Arquitectura.md
- Diagrama de Componentes
- Diagrama de Flujo de Verificación

Flujo principal:

```text
Cliente
   ↓
JWT Authentication
   ↓
Validación de archivos
   ↓
OCR DNI
   ↓
Validación de datos extraídos
   ↓
Face Matching
   ↓
Auditoría
   ↓
Respuesta JSON
```

---

# 4. Análisis STRIDE

| Categoría STRIDE | Amenaza Específica | Componente Afectado | Impacto | Mitigación Propuesta | Prioridad |
|-----------------|-------------------|--------------------|----------|----------------------|------------|
| Spoofing | Uso de DNI perteneciente a otra persona | OCR + Face Matching | Suplantación de identidad | Comparación facial selfie vs foto del DNI mediante DeepFace | Alta |
| Spoofing | Uso de JWT robado o falsificado | API REST | Acceso no autorizado | Validación de firma JWT y expiración de token | Alta |
| Tampering | Modificación de imágenes antes del envío | OCR Service | Extracción de información falsa | Validación de formato, tamaño y consistencia de datos | Alta |
| Tampering | Manipulación de parámetros de la solicitud | API REST | Alteración de resultados | Validación de entradas mediante Pydantic | Media |
| Repudiation | Usuario niega haber realizado una verificación | Audit Service | Pérdida de trazabilidad | Registro de Request ID, fecha y resultado | Alta |
| Information Disclosure | Exposición de datos personales del DNI | API REST | Fuga de información sensible | Respuestas controladas y minimización de datos expuestos | Alta |
| Information Disclosure | Exposición de rutas internas o stack traces | API REST | Divulgación de información interna | Manejo seguro de excepciones | Media |
| Denial of Service | Envío masivo de solicitudes | API REST | Degradación del servicio | Rate Limiting por IP | Alta |
| Denial of Service | Carga de archivos excesivamente grandes | Upload Service | Consumo de recursos | Restricción de tamaño máximo de archivo | Alta |
| Elevation of Privilege | Acceso a endpoints protegidos sin autorización | API REST | Escalamiento de privilegios | Middleware de autenticación JWT | Alta |

---

# 5. Amenazas Adicionales Consideradas

Además de STRIDE, se identificaron amenazas comunes en aplicaciones web modernas.

| Amenaza | Riesgo | Mitigación |
|----------|---------|------------|
| Inyección de datos maliciosos | Alteración de procesamiento interno | Validación estricta mediante Pydantic |
| Enumeración de endpoints | Descubrimiento de funcionalidades internas | Protección mediante autenticación |
| Archivos maliciosos | Ejecución inesperada o corrupción | Lista blanca de extensiones permitidas |
| Fuerza bruta | Intentos repetitivos de acceso | Rate Limiting |
| Exposición de archivos temporales | Acceso a imágenes procesadas | Eliminación automática de temporales |

---

# 6. Controles de Seguridad Definidos

## Seguridad de Autenticación

- JWT obligatorio para consumir la API.
- Tokens con expiración configurable.
- Rechazo automático de tokens inválidos.

---

## Seguridad de Archivos

Formatos permitidos:

- JPG
- JPEG
- PNG

Restricciones:

- Tamaño máximo: 5 MB
- Validación MIME Type
- Validación de extensión

---

## Seguridad de Entradas

Se implementará:

- Validación mediante Pydantic.
- Sanitización de parámetros.
- Verificación de tipos de datos.

---

## Seguridad de Respuestas

No se expondrán:

- Stack traces.
- Rutas internas.
- Información sensible del servidor.

Ejemplo:

Respuesta segura:

```json
{
  "error": "Invalid request"
}
```

Respuesta insegura:

```json
{
  "error": "Traceback...",
  "path": "/usr/local/app/main.py"
}
```

---

## Seguridad de Almacenamiento Temporal

Las imágenes recibidas serán eliminadas una vez finalizado el proceso de validación.

Objetivos:

- Reducir exposición de datos sensibles.
- Evitar acumulación de archivos.
- Minimizar riesgos de acceso no autorizado.

---

# 7. Riesgos Priorizados

Los riesgos más relevantes para la Exposición Parcial son:

| Riesgo | Nivel |
|----------|---------|
| Suplantación de identidad | Alto |
| Robo de JWT | Alto |
| Fuga de datos personales | Alto |
| Denial of Service | Alto |
| Manipulación de documentos | Alto |

---

# 8. Amenazas Fuera del Alcance de la Presentación

Las siguientes amenazas se consideran para futuras fases del proyecto:

| Amenaza | Estado |
|----------|---------|
| Integración con RENIEC | Fase futura |
| Liveness Detection Avanzado | Fase futura |
| Detección de Deepfakes | Fase futura |
| Detección avanzada de fraude documental | Fase futura |
| Validación contra fuentes gubernamentales | Fase futura |

---

# 9. Conclusiones

La metodología STRIDE permitió identificar las principales amenazas que afectan al sistema FaceDocVerify durante su fase inicial de desarrollo.

Como resultado del análisis se definieron controles de seguridad enfocados en:

- Autenticación segura mediante JWT.
- Validación estricta de entradas.
- Protección frente a ataques de denegación de servicio.
- Prevención de exposición de información sensible.
- Trazabilidad mediante auditoría.
- Reducción del riesgo de suplantación de identidad.

Estos controles serán implementados progresivamente durante las semanas S2, S3 y S4 como parte de la construcción de la Presentación.