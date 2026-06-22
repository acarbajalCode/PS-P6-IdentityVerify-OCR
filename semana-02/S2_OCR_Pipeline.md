# S2_OCR_Pipeline.md

# Semana 2 — Implementación del Pipeline OCR

## Objetivo

Implementar el componente OCR del proyecto FaceDocVerify para extraer información relevante de documentos de identidad utilizando herramientas Open Source, aplicando principios de programación segura.

---

# Entorno de Desarrollo

## Sistema Operativo

Windows 11

## Python

Python 3.11.9

## OCR

Tesseract OCR 5.5.0

## Librerías Instaladas

* opencv-python
* pytesseract
* easyocr
* pillow
* numpy
* pytest

---

# Estructura del Proyecto

```text
FaceDocVerify/
│
├── src/
├── tests/
├── docs/
├── logs/
└── venv/
```

---

# Objetivos Funcionales de la Semana 2

Implementar la extracción de:

* Número de DNI
* Nombres
* Apellido paterno
* Apellido materno
* Fecha de nacimiento
* Fecha de vencimiento

Además se validará:

* Mayoría de edad
* Vigencia del documento

---

# Herramientas Seleccionadas

## Tesseract OCR

Motor OCR principal para reconocimiento de texto.

### Motivos de selección

* Open Source
* Amplio soporte
* Compatible con idioma español
* Fácil integración con Python

## EasyOCR

Motor OCR secundario (fallback).

### Motivos de selección

* Mejor desempeño en imágenes complejas
* Basado en Deep Learning
* Complementa a Tesseract

---

# Estado Actual

✅ Entorno configurado

✅ Dependencias instaladas

⏳ Pendiente: Implementación del preprocesamiento de imágenes

⏳ Pendiente: Implementación de extracción OCR

⏳ Pendiente: Medición de precisión


---

# Decisiones de Diseño Adoptadas

## Soporte de documentos

La solución FaceDocVerify soportará inicialmente:

* DNI Azul del Perú
* DNI Electrónico (DNIe)

## Estrategia de extracción

La extracción de información no dependerá de coordenadas fijas dentro del documento.

Se utilizará una estrategia basada en:

1. Preprocesamiento de imagen mediante OpenCV.
2. Extracción OCR mediante Tesseract.
3. OCR de respaldo mediante EasyOCR.
4. Identificación de campos mediante expresiones regulares y reglas de negocio.

Esta aproximación permite una mayor flexibilidad frente a variaciones de formato, rotaciones moderadas y diferencias en la calidad de captura de imágenes.

## Campos objetivo

El sistema buscará identificar:

* Número de DNI.
* Nombres.
* Apellido paterno.
* Apellido materno.
* Fecha de nacimiento.
* Fecha de vencimiento.

## Validaciones derivadas

A partir de los datos extraídos se realizarán:

* Validación de mayoría de edad.
* Validación de vigencia del documento.
* Validación de formato del número de DNI.

---

# Diseño del Módulo de Preprocesamiento

## Objetivo

Mejorar la calidad visual de las imágenes antes de ejecutar el proceso OCR, incrementando la probabilidad de reconocimiento correcto de caracteres.

## Flujo de procesamiento

Imagen Original
↓
Escala de Grises
↓
Reducción de Ruido
↓
Binarización
↓
Imagen Optimizada para OCR

## Técnicas seleccionadas

### Conversión a escala de grises

Reduce la complejidad de la imagen eliminando información de color innecesaria para el reconocimiento de texto.

### Reducción de ruido

Se aplicará desenfoque Gaussiano para disminuir pequeñas variaciones de color y artefactos visuales.

### Binarización

Se transformará la imagen a blanco y negro para maximizar el contraste entre texto y fondo.

## Beneficios esperados

* Mayor precisión OCR.
* Menor sensibilidad a condiciones de iluminación.
* Mejor identificación de números y fechas.
* Mayor compatibilidad con imágenes capturadas desde dispositivos móviles.


---

# Implementación del Módulo OCR

## DocumentScanner

Se implementó una clase responsable de coordinar el proceso de extracción de texto desde documentos de identidad.

### Flujo

Imagen
↓
Preprocesamiento OpenCV
↓
Tesseract OCR
↓
Texto Extraído

## Idioma OCR

Se configuró inicialmente el idioma español (spa) para mejorar el reconocimiento de caracteres propios de documentos peruanos.

### Beneficios

* Mejor reconocimiento de nombres y apellidos.
* Mejor identificación de caracteres acentuados.
* Mayor precisión en documentos emitidos en idioma español.
---

# Verificación del Entorno OCR

Se verificó correctamente la instalación del motor Tesseract OCR versión 5.5 y la disponibilidad del idioma español (spa).

Resultado:

- eng
- enm
- osd
- spa

La disponibilidad del idioma español permitirá mejorar el reconocimiento de caracteres utilizados en documentos peruanos, incluyendo nombres, apellidos y fechas.

---

# Primera Prueba OCR Exitosa

Se realizó una prueba inicial utilizando una imagen real de DNI.

Resultado obtenido:

* Se identificaron correctamente nombres y apellidos.
* Se detectaron fechas presentes en el documento.
* Se obtuvo texto legible suficiente para posteriores procesos de extracción estructurada.

Observación:

La extracción inicial presenta algunos errores de interpretación numérica, lo cual es esperado en motores OCR genéricos. Estos errores serán tratados posteriormente mediante:

* Expresiones regulares (Regex).
* Reglas de negocio.
* Validaciones de formato.

Conclusión:

El pipeline OpenCV + Tesseract se encuentra operativo y listo para la siguiente fase de extracción de campos específicos.


---

# Diseño del Módulo DNI Parser

## Objetivo

Transformar el texto generado por el OCR en una estructura de datos utilizable por el sistema.

## Responsabilidades

* Identificar número de DNI.
* Identificar nombres y apellidos.
* Identificar fechas relevantes.
* Aplicar reglas de validación de formato.
* Retornar información estructurada para etapas posteriores.

## Beneficios

La separación entre OCR y Parser permite desacoplar el reconocimiento de texto de la lógica de negocio, facilitando futuras mejoras y mantenimiento del sistema.

## Flujo

Texto OCR
↓
Expresiones Regulares
↓
Validaciones
↓
Objeto estructurado
↓
Consumo por API y módulos de verificación
## Observaciones de la Primera Extracción

Durante las pruebas se observó que el OCR identifica correctamente números de DNI y fechas principales del documento.

Sin embargo, algunos campos numéricos pueden presentar errores de reconocimiento debido a:

* Calidad de captura de la imagen.
* Condiciones de iluminación.
* Similitud visual entre ciertos caracteres numéricos.

Por este motivo se implementará una capa adicional de validación mediante expresiones regulares y reglas de negocio para mejorar la precisión de los datos extraídos.

---

# Campos Objetivo del DNI Peruano

Para la primera versión funcional del sistema se definieron los siguientes campos obligatorios:

| Campo | Obligatorio |
|---------|---------|
| Número DNI | Sí |
| Apellido paterno | Sí |
| Apellido materno | Sí |
| Nombres | Sí |
| Fecha de nacimiento | Sí |
| Fecha de emisión | No |
| Fecha de vencimiento | Sí |

Estos campos permitirán implementar las validaciones de negocio requeridas por el proyecto:

- Verificación de identidad.
- Validación de mayoría de edad.
- Validación de vigencia del documento.
- Comparación biométrica facial.

## Mejoras de Preprocesamiento

Con el objetivo de aumentar la precisión del OCR sobre documentos de identidad peruanos, se incorporaron técnicas adicionales de preprocesamiento:

- Conversión a escala de grises.
- Redimensionamiento de imagen (200%).
- Reducción de ruido mediante Gaussian Blur.
- Binarización adaptativa.

Estas técnicas permiten mejorar la legibilidad de campos pequeños como fechas, nombres y apellidos presentes en el DNI.

Las pruebas realizadas demostraron que los documentos generados directamente desde PDF conservan mejor la estructura textual del DNI electrónico peruano. Esto permitió que Tesseract identificara correctamente la zona MRZ (Machine Readable Zone), mejorando significativamente la extracción de datos respecto a capturas de pantalla.

## Utilidades OCR

Se creó el módulo:

src/utils/text_utils.py

Responsabilidades:

- Limpieza y normalización de texto OCR.
- Extracción de fechas.
- Cálculo de edad.
- Validación de mayoría de edad.
- Validación de vigencia documental.

Esto permite desacoplar la lógica de negocio del parser principal y facilita futuras ampliaciones del sistema.

# Fix Final
-------------------
### Cara frontal (OCR)

Se extrae información visual del documento:

- Apellidos
- Nombres
- Fecha de emisión (cuando es legible)
- Número de DNI (con ruido posible)

### Cara posterior (MRZ)

Se extrae información estructurada:

- Número de DNI (fuente principal)
- Fecha de nacimiento
- Fecha de vencimiento
- Datos codificados MRZ
  

Reglas de consolidación

- MRZ tiene prioridad en:
  - DNI
  - Fecha de nacimiento
  - Fecha de vencimiento

- OCR frontal complementa:
  - Apellidos
  - Nombres
  - Fecha de emisión

- Se normalizan fechas al formato:
  - DD/MM/YYYY

- Se calcula automáticamente:
  - Edad
  - Estado de mayoría de edad
  - Vigencia del documento

---

Componentes completados:

- ImagePreprocessor ✔
- DocumentScanner ✔
- DNIParser ✔
- MRZParser ✔
- IdentityValidator ✔
- text_utils ✔

Funcionalidades:

- OCR frontal funcional ✔
- OCR posterior funcional ✔
- Consolidación de identidad ✔
- Validación de edad ✔
- Validación de vigencia ✔

---

             ┌──────────────────────────┐
             │  DNI (Cara Frontal)      │
             └─────────────┬────────────┘
                           ↓
                 DocumentScanner
                           ↓
                 ImagePreprocessor
                           ↓
                        OCR (Tesseract)
                           ↓
                      DNIParser
                           ↓
                 Datos OCR estructurados
                           │
                           │
                           ▼
             ┌──────────────────────────┐
             │  DNI (Cara Posterior)    │
             └─────────────┬────────────┘
                           ↓
                 DocumentScanner
                           ↓
                 ImagePreprocessor
                           ↓
                        OCR (Tesseract)
                           ↓
                       MRZParser
                           ↓
                  Datos MRZ estructurados
                           │
                           ▼
                ┌───────────────────┐
                │ IdentityValidator │
                └─────────┬─────────┘
                          ↓
             Consolidación de identidad final


Flujo de procesamiento detallado

###  Procesamiento de cara frontal (OCR)

La cara frontal se procesa mediante OCR para extraer información visual:

- Apellido paterno
- Apellido materno
- Nombres
- Fecha de emisión (cuando es legible)
- Número de DNI (puede contener ruido)

Resultado intermedio:
→ DNIParser (estructura inicial de datos)

---

###  Procesamiento de cara posterior (MRZ)

La cara posterior contiene la zona MRZ, que es la fuente más confiable del sistema:

- Número de DNI (clave principal)
- Fecha de nacimiento
- Fecha de vencimiento
- Datos codificados en formato MRZ

Resultado intermedio:
→ MRZParser (datos altamente confiables)

---

##  Consolidación de datos (IdentityValidator)

El componente IdentityValidator es el núcleo del sistema.

Su función es:

###  Unificación de fuentes

- Fusiona datos de:
  - DNIParser (OCR frontal)
  - MRZParser (posterior)

---

###  Reglas de prioridad

- MRZ tiene prioridad en:
  - Número de DNI
  - Fecha de nacimiento
  - Fecha de vencimiento

- OCR frontal complementa:
  - Apellidos
  - Nombres
  - Fecha de emisión

---

###  Resolución de inconsistencias

Cuando existen diferencias entre OCR y MRZ:

- Se selecciona MRZ como fuente confiable
- OCR se usa solo como respaldo o enriquecimiento

---

###  Normalización de datos

- Fechas convertidas a formato:
  - DD/MM/YYYY

- Limpieza de caracteres OCR ruidosos

---

##  Utilidades de soporte (text_utils)

Se implementa un módulo auxiliar:

src/utils/text_utils.py

Funciones principales:

- Limpieza de texto OCR
- Extracción de fechas desde texto libre
- Cálculo de edad
- Validación de mayoría de edad
- Validación de vigencia documental
- Normalización de formatos entre OCR y MRZ

---

## Resultado del pipeline

El resultado final es un único objeto consolidado:

```json
{
 "dni_number": "77466254",
 "apellido_paterno": "CARBAJAL",
 "apellido_materno": "CAMPOMANES",
 "nombres": "ARMANDO JHEFERSON",
 "fecha_nacimiento": "18/05/1996",
 "fecha_emision": "-----",
 "fecha_vencimiento": "-------",
 "edad": 30,
 "mayor_de_edad": true,
 "documento_vigente": true
}

## 8. Conclusión

Se implementó exitosamente un pipeline de verificación de identidad basado en dos fuentes de información (OCR frontal y MRZ posterior), logrando consolidación automática de datos y validaciones básicas de identidad.