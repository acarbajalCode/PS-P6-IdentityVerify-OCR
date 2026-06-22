# S1_Setup_Entorno.md

# FaceDocVerify
## Configuración del Entorno de Desarrollo

### Curso
Programación Segura

### Proyecto

**FaceDocVerify: A Multi-Modal Secure Identity Verification Framework Integrating Open-Source OCR and Deep Learning Facial Recognition with Real-Time Fraud Detection for Digital Onboarding Processes**

---

# 1. Objetivo

Configurar un entorno de desarrollo seguro, reproducible y compatible con los componentes que serán implementados durante las semanas S2, S3 y S4 del proyecto FaceDocVerify.

---

# 2. Requisitos de Hardware

## Requisitos mínimos

| Recurso | Especificación |
|----------|----------|
| Procesador | Intel Core i5 8va generación o equivalente |
| Memoria RAM | 8 GB |
| Almacenamiento libre | 10 GB |
| Cámara web | Opcional (para pruebas futuras) |
| Sistema Operativo | Windows 10/11, Ubuntu 22.04 o superior |

---

## Recomendado

| Recurso | Especificación |
|----------|----------|
| Procesador | Intel Core i7 o Ryzen 7 |
| Memoria RAM | 16 GB |
| Almacenamiento SSD | 20 GB libres |
| Cámara web HD | Sí |

---

# 3. Software Requerido

| Herramienta | Versión |
|-------------|----------|
| Python | 3.11.x |
| Git | Última estable |
| Visual Studio Code | Última estable |
| Tesseract OCR | 5.x |
| Postman | Última estable |
| Draw.io | Última estable |

---

# 4. Estructura Inicial del Proyecto

```text
FaceDocVerify/
│
├── src/
│   ├── api/
│   ├── auth/
│   ├── ocr/
│   ├── face_recognition/
│   ├── services/
│   └── utils/
│
├── tests/
│   ├── fixtures/
│   └── unit/
│
├── docs/
│   ├── S1/
│   ├── S2/
│   ├── S3/
│   └── S4/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 5. Creación del Entorno Virtual

## Windows

```bash
python -m venv .venv
```

Activar:

```bash
.venv\Scripts\activate
```

---

## Linux

```bash
python3 -m venv .venv
```

Activar:

```bash
source .venv/bin/activate
```

---

# 6. Dependencias Iniciales

Las dependencias definidas corresponden al alcance de la Exposición Parcial.

```txt
fastapi
uvicorn
python-jose
passlib
python-multipart

opencv-python

pytesseract
easyocr

deepface

pydantic

pytest
```

---

# 7. Verificación del Entorno

## Python

```bash
python --version
```

Resultado esperado:

```text
Python 3.11.x
```

---

## Git

```bash
git --version
```

Resultado esperado:

```text
git version x.x.x
```

---

## Tesseract

```bash
tesseract --version
```

Resultado esperado:

```text
tesseract 5.x.x
```

---

# 8. Herramientas Seleccionadas

## FastAPI

Propósito:

- Construcción de API REST.
- Documentación automática Swagger.
- Validación de datos.

Razón de selección:

- Ligera.
- Moderna.
- Amplio soporte para Python.

---

## Tesseract OCR

Propósito:

- Extracción de texto desde imágenes de DNI.

Razón de selección:

- Open Source.
- Alta adopción industrial.
- Compatible con Python.

---

## EasyOCR

Propósito:

- Motor OCR alternativo cuando Tesseract no obtenga resultados satisfactorios.

Razón de selección:

- Mejor desempeño en imágenes complejas.

---

## DeepFace

Propósito:

- Comparación facial entre selfie y fotografía del documento.

Razón de selección:

- Biblioteca open source ampliamente utilizada.
- Permite evaluar múltiples modelos.

---

## OpenCV

Propósito:

- Procesamiento de imágenes.
- Preprocesamiento para OCR.

Razón de selección:

- Estándar de facto en visión computacional.

---

# 9. Configuración de Git

Inicializar repositorio:

```bash
git init
```

Configurar rama principal:

```bash
git branch -M main
```

---

# 10. Estrategia de Ramas

| Rama | Propósito |
|--------|----------|
| main | Versión estable |
| feature/s1-setup-stride | Semana 1 |
| feature/s2-ocr-pipeline | Semana 2 |
| feature/s3-face-recognition | Semana 3 |
| feature/s4-ep-integration | Semana 4 |

---

# 11. Evidencias Requeridas

Capturar:

- Instalación de Python.
- Instalación de Git.
- Instalación de Tesseract.
- Estructura del proyecto.
- Creación del entorno virtual.
- Activación del entorno virtual.
- Ejecución de comandos de verificación.

Guardar imágenes en:

```text
docs/S1/evidencias/
```

---

# 12. Conclusiones

El entorno de desarrollo ha sido definido utilizando herramientas open source y compatibles con los objetivos del proyecto.

La configuración permitirá implementar durante las siguientes semanas:

- OCR para extracción de datos del DNI.
- Reconocimiento facial.
- API REST segura.
- Controles de seguridad definidos en el modelo STRIDE.

Todo el entorno se encuentra alineado con los principios del curso de Programación Segura.