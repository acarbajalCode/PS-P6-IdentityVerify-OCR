# S1_Requisitos.md

# FaceDocVerify

## Requisitos del Sistema

### Proyecto

**FaceDocVerify: Sistema Seguro de Verificación de Identidad utilizando OCR Open Source y Reconocimiento Facial con Mecanismos de Detección de Fraude**

---

# 1. Introducción

FaceDocVerify es una plataforma de verificación de identidad digital orientada a procesos de onboarding seguro. El sistema permitirá validar la identidad de un usuario mediante el análisis de una imagen de documento de identidad (DNI) y una fotografía tipo selfie, utilizando técnicas de OCR y reconocimiento facial.

El proyecto está alineado con los principios de Programación Segura, incorporando mecanismos de autenticación, validación de entradas, auditoría y protección de datos personales.

---

# 2. Objetivo General

Diseñar e implementar un sistema seguro de verificación de identidad utilizando herramientas Open Source para la extracción de información documental y comparación biométrica facial, permitiendo validar la autenticidad de un usuario durante procesos de registro digital.

---

# 3. Alcance del Proyecto

El sistema permitirá:

* Recibir dos imágenes del documento de identidad:
  - Cara frontal del DNI
  - Cara posterior del DNI (MRZ)
* Extraer información relevante mediante OCR.
* Recibir una fotografía tipo selfie.
* Comparar el rostro del documento con la selfie.
* Validar reglas básicas de negocio.
* Retornar un resultado de verificación.
* Registrar eventos de auditoría.

---

# 4. Requisitos Funcionales

## RF01 – Autenticación

El sistema deberá autenticar clientes mediante tokens JWT antes de permitir el acceso a los servicios de verificación.

---

## RF02 – Recepción de documentos

El sistema deberá permitir la carga de dos imágenes del documento de identidad:
- Cara frontal del DNI
- Cara posterior del DNI (MRZ)

Formatos iniciales:

* JPG
* JPEG
* PNG

---

## RF03 – Extracción OCR

El sistema deberá extraer del documento los siguientes campos:

* Número de DNI
* Nombres
* Apellido paterno
* Apellido materno
* Fecha de nacimiento
* Fecha de vencimiento

---

## RF04 – Validación de mayoría de edad

El sistema deberá calcular automáticamente la edad del usuario a partir de la fecha de nacimiento extraída.

Resultado:

* Mayor de edad
* Menor de edad

---

## RF05 – Validación de vigencia del documento

El sistema deberá verificar si la fecha de vencimiento del documento es válida respecto a la fecha actual.

Resultado:

* Documento vigente
* Documento vencido

---

## RF06 – Recepción de selfie

El sistema deberá permitir la carga de una fotografía tipo selfie para comparación biométrica.

---

## RF07 – Comparación facial

El sistema deberá comparar la fotografía del documento con la selfie utilizando modelos de reconocimiento facial.

Resultado:

* Coincide
* No coincide

Además deberá retornar un puntaje de similitud.

---

## RF08 – Resultado de verificación

El sistema deberá generar una respuesta consolidada con los resultados obtenidos durante el proceso de validación.

---

## RF09 – Auditoría

El sistema deberá registrar información básica de auditoría para cada solicitud procesada.

Datos mínimos:

* Request ID
* Fecha y hora
* Resultado de la verificación

## RF10 – Validación del número de DNI

El sistema deberá verificar que el número de DNI extraído contenga exactamente ocho dígitos numéricos.

Resultado:

* Válido
* Inválido

## RF11 – Eliminación de archivos temporales

El sistema deberá eliminar automáticamente las imágenes temporales utilizadas durante el proceso de verificación una vez finalizada la operación.

---

# 5. Requisitos No Funcionales

## RNF01 – Seguridad

El acceso a los servicios deberá estar protegido mediante autenticación JWT.

---

## RNF02 – Validación de archivos

El sistema deberá validar:

* Extensión
* Tipo MIME
* Tamaño máximo permitido

antes de procesar cualquier imagen.

---

## RNF03 – Protección de información

Los mensajes de error no deberán exponer información sensible del sistema.

---

## RNF04 – Disponibilidad

El sistema deberá responder adecuadamente a solicitudes válidas sin afectar la estabilidad del servicio.

---

## RNF05 – Auditoría

Las operaciones críticas deberán quedar registradas para fines de trazabilidad.

---

## RNF06 – Escalabilidad

La arquitectura deberá permitir futuras integraciones con:

* RENIEC
* SBS
* Servicios KYC
* Sistemas externos

## RNF07 –(Límite de tamaño) Restricción de tamaño de archivo

El sistema deberá aceptar únicamente imágenes cuyo tamaño no exceda los 5 MB.


## RNF08 –(Trazabilidad) Identificador único de operación

Cada solicitud procesada deberá generar un identificador único (Request ID) para fines de auditoría y seguimiento.

---

# 6. Supuestos

* Se utilizarán documentos sintéticos durante las pruebas.
* No existirá integración directa con RENIEC.
* No se almacenarán imágenes permanentemente durante la presentación.
* El sistema operará inicialmente en entorno local.

---

# 7. Restricciones

* El proyecto utilizará únicamente herramientas Open Source durante las primeras fases.
* No se utilizarán APIs comerciales de OCR o reconocimiento facial.
* La presentación cubrirá únicamente funcionalidades implementadas hasta la Semana 4.

---

# 8. Criterios de Éxito para la Presentación

La presentación será considerada satisfactoria si el sistema logra:

- Extrae información de la cara frontal del DNI mediante OCR
- Extrae información de la cara posterior mediante MRZ
- Consolida ambas fuentes en un solo JSON
- Calcula edad y vigencia del documento
- Protege endpoints mediante JWT (base del sistema)
Se asume que el DNI será procesado en dos imágenes separadas:

- Frontal
- Posterior (MRZ visible)