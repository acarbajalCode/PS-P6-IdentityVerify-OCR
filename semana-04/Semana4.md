# Semana 4 — Endpoint de Integración y Seguridad (EP Integration)

## Proyecto

**FaceDocVerify**

## Rama de trabajo

```bash
feature/s4-ep-integration
```

## Objetivo de la Semana 4

Implementar un endpoint REST que permita validar la identidad de un usuario mediante:

* Lectura OCR de DNI.
* Extracción de datos MRZ.
* Comparación biométrica facial.
* Detección de liveness.
* Protección mediante JWT.
* Registro de auditoría.
* Eliminación segura de archivos temporales.

---

# Funcionalidades Implementadas

## Endpoint Principal

Se implementó el endpoint:

```http
POST /api/v1/verify-identity
```

Este endpoint recibe:

* Foto frontal del DNI.
* Foto posterior del DNI.
* Selfie del usuario.

Procesa la información y devuelve un resultado consolidado de validación.

---

## Endpoint de Login

Se implementó el endpoint:

```http
POST /api/v1/login
```

Permite autenticar usuarios y generar tokens JWT.

Ejemplo de solicitud:

```json
{
  "username": "admin",
  "password": "1234"
}
```

Respuesta:

```json
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
```

---

# Seguridad Implementada

## JWT Authentication

Se implementó autenticación basada en JWT.

Flujo:

1. Usuario realiza login.
2. API genera token JWT.
3. Cliente envía token mediante:

```http
Authorization: Bearer <token>
```

4. API valida el token antes de ejecutar el proceso biométrico.

---

## Validación de Token

Casos probados:

### Token válido

Resultado:

```http
200 OK
```

### Token inválido

Resultado:

```http
401 Unauthorized
```

Respuesta:

```json
{
  "detail": "Invalid or expired token"
}
```

### Sin token

Resultado:

```http
401 Unauthorized
```

Respuesta:

```json
{
  "detail": "Not authenticated"
}
```

---

# Validación de Archivos

Se implementó validación de:

## Tipos permitidos

```text
image/jpeg
image/png
```

## Tamaño máximo

```text
5 MB
```

Archivos inválidos generan:

```http
400 Bad Request
```

---

# OCR y Extracción de Identidad

Se integraron:

* DocumentScanner
* MRZParser
* DNIParser
* IdentityValidator

Información obtenida:

* Número de DNI.
* Apellidos.
* Nombres.
* Fecha de nacimiento.
* Fecha de vencimiento.
* Edad.
* Mayor de edad.
* Estado de vigencia del documento.

---

# Face Matching

Se integró:

```python
FaceMatcher
```

Resultado devuelto:

```json
{
  "match": true,
  "distance": 0.475761,
  "threshold": 0.68,
  "model": "ArcFace"
}
```

---

# Liveness Detection

Se integró:

```python
LivenessDetector
```

Ejemplo:

```json
{
  "live": true,
  "reason": "face_likely_real"
}
```

---

# Auditoría

Se implementó auditoría en:

```text
audit_log.jsonl
```

Información almacenada:

* request_id
* timestamp
* client_ip
* usuario autenticado
* resultado OCR
* resultado biométrico
* resultado liveness
* access_granted

Ejemplo:

```json
{
  "request_id": "...",
  "timestamp": "...",
  "client_ip": "127.0.0.1",
  "user": "admin",
  "access_granted": false
}
```

Cada solicitud genera una nueva línea en el archivo.

---

# Eliminación de Archivos Temporales

Luego del procesamiento se eliminan:

```text
front_*.jpg
back_*.jpg
selfie_*.jpg
```

Verificado durante las pruebas.

---

# Pruebas Realizadas

## Prueba 1 — Usuario válido

Resultado:

* JWT generado correctamente.
* OCR exitoso.
* Face Match exitoso.
* Liveness exitoso.
* Access Granted = true.

Resultado:

```http
200 OK
```

---

## Prueba 2 — Token inválido

Resultado esperado:

```http
401 Unauthorized
```

Resultado obtenido:

Correcto.

---

## Prueba 3 — Sin token

Resultado esperado:

```http
401 Unauthorized
```

Resultado obtenido:

Correcto.

---

## Prueba 4 — Rostro diferente al DNI

Resultado obtenido:

```json
{
  "face_match": {
    "match": false
  },
  "access_granted": false
}
```

Comportamiento correcto.

---

# Evidencias

## Swagger

```text
http://127.0.0.1:8000/docs
```

## Login

```text
POST /api/v1/login
```

## Verificación de identidad

```text
POST /api/v1/verify-identity
```

## Auditoría

```text
audit_log.jsonl
```

---

# Checklist Semana 4

| Item                       | Estado |
| -------------------------- | ------ |
| Endpoint funcional         | ✅      |
| OCR integrado              | ✅      |
| MRZ integrado              | ✅      |
| Face Match integrado       | ✅      |
| Liveness integrado         | ✅      |
| JWT activo                 | ✅      |
| Login implementado         | ✅      |
| Auditoría implementada     | ✅      |
| Limpieza de temporales     | ✅      |
| Swagger operativo          | ✅      |
| Pruebas Postman realizadas | ✅      |

---

# Conclusión

La Semana 4 concluye con la implementación completa del endpoint de verificación de identidad, incluyendo autenticación JWT, procesamiento OCR, validación biométrica, auditoría y pruebas funcionales realizadas mediante Swagger y Postman. El sistema se encuentra listo para ser consumido por aplicaciones externas mediante autenticación basada en token.
