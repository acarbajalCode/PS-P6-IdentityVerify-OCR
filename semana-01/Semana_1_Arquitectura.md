# S1_Arquitectura.md

# FaceDocVerify

## Arquitectura del Sistema

---

# 1. Introducción

FaceDocVerify es un sistema de verificación de identidad digital diseñado bajo principios de Programación Segura. Su objetivo es validar la identidad de un usuario mediante el análisis de una imagen de documento de identidad (DNI) y una fotografía tipo selfie, utilizando tecnologías Open Source de OCR y reconocimiento facial.

La arquitectura propuesta busca garantizar modularidad, seguridad, mantenibilidad y escalabilidad para futuras integraciones con servicios externos de validación de identidad.

---

# 2. Objetivo de la Arquitectura

Definir la estructura lógica del sistema, los componentes involucrados y el flujo de procesamiento de información para realizar verificaciones de identidad de forma segura y eficiente.

---

# 3. Principios de Diseño

La arquitectura de FaceDocVerify se basa en los siguientes principios:

* Separación de responsabilidades.
* Diseño modular.
* Programación segura.
* Minimización de datos sensibles.
* Escalabilidad futura.
* Uso de herramientas Open Source.
* Trazabilidad y auditoría de operaciones.

---

# 4. Arquitectura General

El sistema está compuesto por los siguientes módulos:

1. Cliente Consumidor
2. API REST Segura
3. Servicio OCR
4. Servicio de Validación
5. Servicio de Reconocimiento Facial
6. Servicio de Auditoría
7. Base de Datos Local

---

# 5. Componentes del Sistema

## 5.1 Cliente Consumidor

Representa cualquier aplicación o usuario autorizado que consuma la API de FaceDocVerify.

Responsabilidades:

* Autenticarse mediante JWT.
* Enviar imagen del DNI.
* Enviar fotografía selfie.
* Recibir el resultado de la verificación.

---

## 5.2 API REST Segura (FastAPI)

Es el punto central de entrada al sistema.

Responsabilidades:

* Validar autenticación JWT.
* Validar formatos de archivos.
* Orquestar el flujo de verificación.
* Retornar respuestas JSON.
* Gestionar errores.

Tecnología:

* FastAPI

---

## 5.3 Servicio OCR

Responsable de extraer información textual del documento de identidad.

Tecnologías:

* Tesseract OCR
* EasyOCR (Fallback)

Campos objetivo:

* Número de DNI
* Nombres
* Apellido paterno
* Apellido materno
* Fecha de nacimiento
* Fecha de vencimiento

---

## 5.4 Servicio de Validación

Responsable de aplicar reglas de negocio sobre la información extraída.

Validaciones iniciales:

### Mayoría de edad

Determina si el usuario posee 18 años o más.

### Vigencia del documento

Determina si la fecha de vencimiento del documento es válida respecto a la fecha actual.

---

## 5.5 Servicio de Reconocimiento Facial

Responsable de comparar la fotografía del documento con la selfie proporcionada por el usuario.

Tecnologías:

* DeepFace
* OpenCV

Resultado esperado:

* Coincidencia facial
* Puntaje de similitud (Similarity Score)

---

## 5.6 Servicio de Auditoría

Responsable de registrar eventos relevantes del proceso.

Información registrada:

* Request ID
* Fecha y hora
* Resultado de la verificación
* Tiempo de procesamiento

---

## 5.7 Base de Datos

Durante las primeras fases del proyecto se utilizará una base de datos local.

Tecnología inicial:

* SQLite

Posible evolución futura:

* PostgreSQL

---

# 6. Flujo General de Verificación

## Paso 1

El cliente obtiene un token JWT válido.

---

## Paso 2

El cliente envía:

* Imagen del DNI.
* Fotografía selfie.

---

## Paso 3

La API valida:

* Autenticación.
* Tipo de archivo.
* Tamaño permitido.

---

## Paso 4

El Servicio OCR extrae la información del documento.

---

## Paso 5

El Servicio de Validación procesa:

* Edad del usuario.
* Vigencia del documento.

---

## Paso 6

El Servicio de Reconocimiento Facial compara:

* Fotografía del DNI.
* Selfie del usuario.

---

## Paso 7

Se calcula el resultado final de la verificación.

---

## Paso 8

Se registra la operación en auditoría.

---

## Paso 9

La API retorna una respuesta JSON al cliente.

---

# 7. Flujo de Decisiones

La lógica de negocio seguirá el siguiente flujo:

1. JWT válido.
2. OCR exitoso.
3. Usuario mayor de edad.
4. Documento vigente.
5. Coincidencia facial aceptable.
6. Resultado final.

Si alguna validación crítica falla, la verificación será rechazada.

---

# 8. Respuesta Esperada del Sistema

Ejemplo de respuesta exitosa:

```json
{
  "request_id": "uuid",
  "dni_number": "12345678",
  "full_name": "Juan Perez Gomez",
  "birth_date": "2000-01-15",
  "is_adult": true,
  "expiration_date": "2032-05-01",
  "document_expired": false,
  "face_match": true,
  "similarity": 0.87,
  "verification_status": "APPROVED"
}
```

Ejemplo de respuesta rechazada:

```json
{
  "request_id": "uuid",
  "verification_status": "REJECTED",
  "reason": "DOCUMENT_EXPIRED"
}
```

---

# 9. Consideraciones de Seguridad

La arquitectura incorpora controles de seguridad desde su diseño:

* Autenticación basada en JWT.
* Validación de archivos recibidos.
* Manejo seguro de errores.
* Auditoría de eventos.
* Minimización de exposición de datos personales.
* Eliminación de archivos temporales luego del procesamiento.

---

# 10. Evolución Futura

La arquitectura permitirá incorporar posteriormente:

* Integración con RENIEC.
* Integración con SBS.
* PostgreSQL.
* Detección avanzada de fraude documental.
* Liveness Detection.
* Despliegue Cloud.
* Hardening avanzado.
