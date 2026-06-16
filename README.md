# PS-P6 — UQ·VerifyID | Secure Identity Verification Platform
### DD281 Programación Segura · Universidad Autónoma del Perú · 2026-1 · UQ AI SOLUTION COMPANY SAC

[![Grupo](https://img.shields.io/badge/Grupo-G6-purple?style=for-the-badge)]()
[![Stack](https://img.shields.io/badge/Stack-Python%20%7C%20FastAPI%20%7C%20Azure-orange?style=for-the-badge)]()
[![Journal](https://img.shields.io/badge/Target-Expert_Systems_with_Applications_Q1-red?style=for-the-badge)]()
[![OCR](https://img.shields.io/badge/OCR-Tesseract%20%7C%20EasyOCR-blue?style=for-the-badge)]()
[![Face](https://img.shields.io/badge/Face-DeepFace%20%7C%20OpenCV-green?style=for-the-badge)]()

---

## 🏆 Los 6 Títulos Scopus Q1 del Curso DD281-2026-1

> Todos los grupos del curso publican su investigación en journals Scopus Q1 al término del ciclo.
> El docente es coautor y guía el proceso de publicación.

| Grupo | Proyecto | Título Scopus Q1 Optimizado | Journal Target | Q |
|:---:|---|---|---|:---:|
| G1 | UQ·SecureID | "Zero-Trust Behavioral Authentication: A Machine Learning-Enhanced Identity Verification Framework with Anomaly Detection for Continuous User Authentication in Cloud-Native Web Applications" | Computers & Security — Elsevier | Q1 |
| G2 | UQ·FinSecure | "SecureFinAPI: A Hybrid Machine Learning and Rule-Based Fraud Detection System for RESTful Banking APIs Compliant with OWASP API Security Top 10" | J. Information Security & Applications — Elsevier | Q1 |
| G3 | UQ·HealthShield | "PrivacyShield: An End-to-End Encrypted Electronic Health Record System with Attribute-Based Access Control for HIPAA and Ley N°29733 Compliance" | J. Biomedical Informatics — Elsevier | Q1 |
| G4 | UQ·CivicVote | "CryptoVote: A Blockchain-Enhanced Electronic Voting Protocol with Zero-Knowledge Proof Verification for Tamper-Resistant and Privacy-Preserving Democratic Processes" | Future Generation Computer Systems — Elsevier | Q1 |
| G5 | UQ·AuditAI | "AutoPenTest-AI: An Artificial Intelligence-Driven Automated Web Penetration Testing Framework with Natural Language Vulnerability Reporting Based on OWASP Top 10" | IEEE Access — IEEE | Q1 |
| **G6** | **UQ·VerifyID** | **"FaceDocVerify: A Multi-Modal Secure Identity Verification Framework Integrating Open-Source OCR and Deep Learning Facial Recognition with Real-Time Fraud Detection for Digital Onboarding Processes"** | Expert Systems with Applications — Elsevier | **Q1** |

---

## 📄 Tu Proyecto: G6 — UQ·VerifyID

### Título Scopus Q1 Optimizado

> **"FaceDocVerify: A Multi-Modal Secure Identity Verification Framework Integrating Open-Source OCR and Deep Learning Facial Recognition with Real-Time Fraud Detection for Digital Onboarding Processes"**
>
> 🎯 **Journal:** Expert Systems with Applications — Elsevier — **Q1** — Impact Factor: **8.5**
> 🔗 **Verificar cuartil:** https://www.scimagojr.com/journalsearch.php?q=Expert+Systems+with+Applications

**Keywords para indexación Scopus:**
`identity verification` · `OCR` · `facial recognition` · `fraud detection` · `deep learning` · `biometric authentication` · `document analysis` · `liveness detection` · `digital onboarding` · `open-source security`

---

### ❗ Problema que Resuelve

El **fraude de identidad digital** es uno de los mayores desafíos de seguridad del siglo XXI:

- En Perú, el **32% de los fraudes bancarios** en 2024 involucró suplantación de identidad en procesos de onboarding digital (SBS, 2024).
- Los sistemas de verificación manual de DNI tienen una tasa de error del **15-20%** (RENIEC, 2023).
- El **78% de las empresas peruanas** que ofrecen servicios digitales carecen de un sistema automatizado de verificación de identidad (INDECOPI, 2024).
- Los sistemas comerciales de KYC (Know Your Customer) cuestan entre **$0.50 y $2.00 por verificación**, prohibitivos para startups peruanas.

**Los problemas técnicos específicos son:**
1. **Sin validación de documento físico:** sistemas aceptan selfies sin verificar que el documento sea auténtico.
2. **Sin liveness detection:** fotos impresas o pantallas pueden engañar a sistemas de reconocimiento facial simples.
3. **Sin detección de manipulación de imagen:** documentos alterados con Photoshop pasan los controles.
4. **Sin integración con fuentes oficiales:** no cruzan datos con RENIEC/SBS para validación final.

**UQ·VerifyID** resuelve esto con un pipeline de 4 capas:
1. **OCR seguro** → Tesseract + EasyOCR para extraer datos del DNI/pasaporte peruano
2. **Reconocimiento facial** → DeepFace (VGG-Face2) para comparar selfie vs foto del documento
3. **Detección de fraude** → modelo XGBoost + reglas heurísticas para detectar documentos alterados
4. **Liveness detection** → análisis de micro-movimientos con OpenCV para detectar ataques de presentación

---

### 🎯 Objetivos del Proyecto

**Objetivo General:**
Diseñar e implementar un sistema de verificación de identidad seguro multi-modal, utilizando herramientas open source (Tesseract, EasyOCR, DeepFace, OpenCV), con detección de fraude en tiempo real, que garantice la autenticidad del documento y la presencia del usuario para procesos de onboarding digital de UQ AI SOLUTION COMPANY SAC.

**Objetivos Específicos:**
1. Implementar un pipeline OCR con Tesseract + EasyOCR capaz de extraer con ≥95% de precisión los campos del DNI peruano (número, nombre, apellidos, fecha de nacimiento, fecha de vencimiento).
2. Integrar DeepFace (modelo VGG-Face2) para comparación facial selfie-vs-documento con umbral de similitud ≥0.80 (cosine similarity).
3. Desarrollar un módulo de liveness detection con OpenCV que detecte ataques de presentación (fotos impresas, pantallas) con ≥90% de accuracy.
4. Construir un clasificador de fraude documental con XGBoost + análisis de metadatos EXIF que detecte manipulaciones de imagen con ≥88% F1-score.
5. Exponer el sistema como API REST segura con FastAPI, con autenticación JWT, rate limiting y cifrado de imágenes en tránsito (TLS 1.3).
6. Desplegar en Azure App Services con Azure Blob Storage para imágenes (cifradas en reposo con AES-256) bajo el dominio `verifyid.uqaisolutions.com.pe`.

---

### 🔬 Metodología

El proyecto sigue la metodología **CRISP-DM adaptada a seguridad** con 4 fases:

```
FASE 1 — THREAT MODELING (S1)
  └─ STRIDE aplicado al pipeline OCR + Face Recognition
  └─ Modelado de amenazas: spoofing, tampering, repudiation

FASE 2 — PIPELINE OCR + FACE (S2–S3)
  └─ Preprocessing de imagen: OpenCV (deskew, denoise, binarize)
  └─ Extracción OCR: Tesseract 5 (LSTM) + EasyOCR (backup)
  └─ Comparación facial: DeepFace (VGG-Face2, cosine similarity)

FASE 3 — FRAUD DETECTION (S4–S5)
  └─ Feature engineering: metadatos EXIF, análisis DCT, ELA (Error Level Analysis)
  └─ Modelo: XGBoost + reglas heurísticas
  └─ Liveness: Optical Flow (Lucas-Kanade) + blink detection

FASE 4 — HARDENING + DEPLOY (S6–S8)
  └─ Security headers, rate limiting, input validation
  └─ Azure deploy + PenTest por G5
  └─ Documentación Scopus Q1
```

**Stack tecnológico:**

| Capa | Tecnología | Propósito |
|---|---|---|
| API | FastAPI 0.111 | Endpoints REST + validación |
| OCR | Tesseract 5.3 + EasyOCR 1.7 | Extracción de texto del DNI |
| Face | DeepFace 0.0.93 + OpenCV 4.9 | Comparación facial + liveness |
| Fraud | XGBoost 2.0 + scikit-learn | Clasificación de documentos |
| DB | PostgreSQL 16 + Azure Blob | Datos + imágenes cifradas |
| Auth | JWT (HS256) + Azure Key Vault | Tokens seguros |
| Deploy | Azure App Services | Westus3 |
| CI/CD | GitHub Actions + Bandit | Pipeline seguro |

---

## 📅 Plan de Desarrollo por Semanas (8 Semanas)

### Visión general

```
S1 → Setup + STRIDE + Dataset DNI
S2 → OCR Pipeline (Tesseract + EasyOCR)
S3 → Reconocimiento Facial (DeepFace + liveness)
S4 ★ EP: Exposición Parcial 60% — Demo pipeline OCR + Face
S5 → Fraud Detection (XGBoost + ELA)
S6 → API Segura + Azure Deploy
S7 → PenTest (G5 audita G6) + Hardening
S8 ★ EF: Presentación Final 100% — Sistema completo
```

---

### Semana 1 — Setup del Entorno + Threat Modeling

**Rama:** `feature/s1-setup-stride`  
**PR hacia:** `main` — requiere aprobación del docente

**Entregables:**
- [ ] Repositorio configurado con estructura completa
- [ ] Entorno virtual Python 3.11 con dependencias base
- [ ] Diagrama de arquitectura del sistema (draw.io o Mermaid)
- [ ] STRIDE threat model del pipeline de verificación
- [ ] Dataset de prueba: 20 imágenes de DNI sintéticos (sin datos reales)
- [ ] `semana-01/STRIDE_ThreatModel.md` — amenazas identificadas por categoría

**Tareas técnicas:**
```bash
# Setup inicial
python -m venv venv
pip install fastapi uvicorn pytesseract easyocr deepface opencv-python xgboost
pip install python-jose[cryptography] python-multipart pillow

# Estructura de carpetas
mkdir -p src/{ocr,face_recognition,fraud_detection,auth,api}
mkdir -p tests docs semana-{01..08}
```

**STRIDE para el pipeline de verificación:**

| Amenaza | Componente afectado | Mitigación |
|---|---|---|
| **S**poofing | Selfie con foto impresa | Liveness detection (blink, movimento) |
| **T**ampering | Imagen DNI modificada | ELA + análisis de metadatos EXIF |
| **R**epudiation | Verificación sin logs | Registro inmutable en Azure Table |
| **I**nformation Disclosure | Imagen DNI en memoria | Cifrado AES-256, borrado tras proceso |
| **D**enial of Service | Subida masiva de imágenes | Rate limiting: 5 req/min por IP |
| **E**levation of Privilege | JWT manipulado | Firma HS256 + expiración 15 min |

**Rúbrica S1 (20 pts):**

| Criterio | Pts |
|---|---|
| Repo creado con estructura correcta | 4 |
| Diagrama de arquitectura completo | 4 |
| STRIDE con ≥5 amenazas identificadas | 6 |
| Dataset sintético de prueba listo | 3 |
| PR aprobado con code review | 3 |

---

### Semana 2 — Pipeline OCR: Extracción de Datos del DNI

**Rama:** `feature/s2-ocr-pipeline`  
**PR hacia:** `main`

**Entregables:**
- [ ] Módulo `src/ocr/document_scanner.py` funcional
- [ ] Preprocessing de imagen (deskew, denoise, binarize) con OpenCV
- [ ] Extracción de campos del DNI peruano con ≥90% accuracy
- [ ] Validación de formato de campos (número DNI, fechas)
- [ ] `semana-02/OCR_Results.md` — métricas de accuracy por campo

**Código base — `src/ocr/document_scanner.py`:**

```python
import cv2
import pytesseract
import easyocr
import re
from pathlib import Path

class DNIScanner:
    """
    Pipeline OCR para extracción segura de datos del DNI peruano.
    Combina Tesseract (primary) + EasyOCR (fallback) para máxima precisión.
    """
    
    def __init__(self):
        self.reader = easyocr.Reader(['es'], gpu=False)
        pytesseract.pytesseract.tesseract_cmd = r'tesseract'
    
    def preprocess(self, image_path: str) -> any:
        """Aplica pipeline de preprocesamiento para mejorar OCR."""
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Deskew + denoise + binarize (Otsu threshold)
        denoised = cv2.fastNlMeansDenoising(gray, h=10)
        _, binary = cv2.threshold(denoised, 0, 255,
                                   cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return binary
    
    def extract_dni_fields(self, image_path: str) -> dict:
        """
        Extrae campos del DNI peruano.
        Returns: {dni_number, nombre, apellidos, fecha_nac, fecha_venc, valid}
        """
        processed = self.preprocess(image_path)
        
        # Tesseract (primary)
        text = pytesseract.image_to_string(processed, lang='spa',
                                            config='--psm 6')
        
        # EasyOCR como fallback si Tesseract falla
        if len(text.strip()) < 20:
            results = self.reader.readtext(image_path)
            text = ' '.join([r[1] for r in results])
        
        return self._parse_dni_fields(text)
    
    def _parse_dni_fields(self, text: str) -> dict:
        """Parsea campos del DNI con regex validados para formato peruano."""
        dni_pattern = r'\b\d{8}\b'
        date_pattern = r'\b\d{2}/\d{2}/\d{4}\b'
        
        dni_matches = re.findall(dni_pattern, text)
        date_matches = re.findall(date_pattern, text)
        
        return {
            'dni_number':   dni_matches[0] if dni_matches else None,
            'fecha_nac':    date_matches[0] if len(date_matches) > 0 else None,
            'fecha_venc':   date_matches[1] if len(date_matches) > 1 else None,
            'raw_text':     text,
            'valid':        bool(dni_matches and len(date_matches) >= 2)
        }
```

**Rúbrica S2 (20 pts):**

| Criterio | Pts |
|---|---|
| Preprocessing con OpenCV funcional | 5 |
| Extracción de DNI number con ≥90% accuracy | 5 |
| Extracción de fechas con ≥85% accuracy | 5 |
| Fallback EasyOCR implementado | 3 |
| Tests unitarios del módulo OCR | 2 |

---

### Semana 3 — Reconocimiento Facial + Liveness Detection

**Rama:** `feature/s3-face-recognition`  
**PR hacia:** `main`

**Entregables:**
- [ ] Módulo `src/face_recognition/face_matcher.py`
- [ ] Comparación selfie vs foto DNI con DeepFace (modelo VGG-Face2)
- [ ] Liveness detection básico con OpenCV (blink detection + Optical Flow)
- [ ] Umbral de similitud configurable (default: 0.80 cosine)
- [ ] `semana-03/Face_Results.md` — accuracy con dataset sintético

**Código base — `src/face_recognition/face_matcher.py`:**

```python
from deepface import DeepFace
import cv2
import numpy as np

class FaceMatcher:
    """
    Comparación facial segura usando DeepFace (VGG-Face2).
    Detecta ataques de presentación mediante liveness detection.
    """
    
    SIMILARITY_THRESHOLD = 0.80
    MODELS = ["VGG-Face", "Facenet512", "ArcFace"]
    
    def verify_identity(self, selfie_path: str, document_photo_path: str) -> dict:
        """
        Compara selfie con foto del documento.
        Usa ensemble de 3 modelos para mayor robustez.
        """
        results = []
        for model in self.MODELS:
            try:
                result = DeepFace.verify(
                    img1_path   = selfie_path,
                    img2_path   = document_photo_path,
                    model_name  = model,
                    distance_metric = 'cosine',
                    enforce_detection = True
                )
                results.append(result['distance'])
            except Exception:
                continue
        
        if not results:
            return {'match': False, 'confidence': 0.0, 'error': 'No face detected'}
        
        avg_distance = np.mean(results)
        similarity   = 1 - avg_distance   # Convertir distancia a similitud
        
        return {
            'match':      similarity >= self.SIMILARITY_THRESHOLD,
            'similarity': round(float(similarity), 4),
            'threshold':  self.SIMILARITY_THRESHOLD,
            'models_used': len(results)
        }
    
    def check_liveness(self, video_frames: list) -> dict:
        """
        Detecta si el usuario es una persona real (no foto/pantalla).
        Analiza movimiento de ojos y variación de píxeles entre frames.
        """
        if len(video_frames) < 5:
            return {'is_live': False, 'reason': 'Insufficient frames'}
        
        # Analizar variación entre frames (foto estática = 0 variación)
        variations = []
        for i in range(1, len(video_frames)):
            diff = cv2.absdiff(video_frames[i-1], video_frames[i])
            variations.append(np.mean(diff))
        
        avg_variation = np.mean(variations)
        is_live = avg_variation > 2.0   # Umbral calibrado experimentalmente
        
        return {
            'is_live':       is_live,
            'avg_variation': round(float(avg_variation), 4),
            'frames_analyzed': len(video_frames)
        }
```

**Rúbrica S3 (20 pts):**

| Criterio | Pts |
|---|---|
| DeepFace integrado con VGG-Face2 | 6 |
| Ensemble de ≥2 modelos para robustez | 4 |
| Liveness detection funcional | 6 |
| Umbral configurable y documentado | 2 |
| Tests con dataset facial sintético | 2 |

---

### Semana 4 ★ — EXPOSICIÓN PARCIAL (EP) — 60%

**Rama:** `feature/s4-ep-integration`  
**PR hacia:** `main`

**Demo requerida:**
1. Subir imagen de DNI sintético → sistema extrae campos con OCR
2. Subir selfie → sistema compara con foto del DNI
3. Mostrar resultado en JSON: `{match: true/false, similarity: 0.87, dni_valid: true}`
4. Mostrar en DevTools que las imágenes se transmiten por HTTPS y no quedan en storage público

**Endpoint de integración — `src/api/main.py`:**

```python
from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.security import HTTPBearer
import uuid, tempfile, os

app = FastAPI(title="UQ·VerifyID API", version="1.0.0-ep")
security = HTTPBearer()

@app.post("/api/v1/verify-identity")
async def verify_identity(
    document: UploadFile = File(..., description="Foto del DNI"),
    selfie:   UploadFile = File(..., description="Foto selfie del usuario"),
    token:    str        = Depends(security)
):
    """
    Pipeline completo de verificación de identidad.
    Paso 1: OCR extrae datos del documento
    Paso 2: Face matching selfie vs foto del documento
    Paso 3: Resultado consolidado
    """
    request_id = str(uuid.uuid4())
    
    # Guardar temporalmente con nombre aleatorio (no el nombre original)
    tmp_dir = tempfile.mkdtemp()
    doc_path  = os.path.join(tmp_dir, f"doc_{request_id}.jpg")
    self_path = os.path.join(tmp_dir, f"self_{request_id}.jpg")
    
    try:
        with open(doc_path, 'wb') as f:
            f.write(await document.read())
        with open(self_path, 'wb') as f:
            f.write(await selfie.read())
        
        # TODO S3: Llamar scanner.extract_dni_fields(doc_path)
        # TODO S3: Llamar matcher.verify_identity(self_path, doc_path)
        
        return {
            "request_id":      request_id,
            "status":          "pending_full_integration",
            "document_valid":  True,   # Placeholder EP
            "face_match":      True,   # Placeholder EP
            "similarity":      0.0,
        }
    finally:
        # SEGURIDAD: Borrar imágenes temporales siempre
        for p in [doc_path, self_path]:
            if os.path.exists(p):
                os.remove(p)

@app.get("/health")
async def health():
    return {"status": "ok", "service": "UQ·VerifyID"}
```

**Rúbrica EP (30 pts):**

| Criterio | Pts |
|---|---|
| Demo funcional: OCR extrae DNI number correctamente | 8 |
| Demo funcional: Face matching retorna similarity score | 8 |
| API endpoint `/verify-identity` responde JSON correcto | 6 |
| Imágenes temporales se eliminan después del proceso | 4 |
| Presentación oral: explica decisiones de seguridad | 4 |

---

### Semana 5 — Fraud Detection: Detección de Documentos Falsificados

**Rama:** `feature/s5-fraud-detection`  
**PR hacia:** `main`

**Entregables:**
- [ ] Módulo `src/fraud_detection/fraud_detector.py`
- [ ] Error Level Analysis (ELA) para detectar manipulación de imagen
- [ ] Análisis de metadatos EXIF (fecha de creación, software editor)
- [ ] Modelo XGBoost entrenado con features de integridad
- [ ] `semana-05/Fraud_Model_Metrics.md` — F1-score, precision, recall

**Código base — `src/fraud_detection/fraud_detector.py`:**

```python
import cv2
import numpy as np
from PIL import Image
import piexif
import xgboost as xgb
from sklearn.preprocessing import StandardScaler

class FraudDetector:
    """
    Detecta documentos de identidad falsificados usando:
    1. ELA (Error Level Analysis) — detecta ediciones con Photoshop/GIMP
    2. Análisis EXIF — detecta software de edición en metadatos
    3. XGBoost — clasificador entrenado con features de integridad
    """
    
    ELA_QUALITY = 90
    ELA_SCALE   = 15
    
    def compute_ela(self, image_path: str) -> float:
        """
        Error Level Analysis: mide diferencia entre imagen original
        y su versión re-comprimida. Las áreas editadas muestran mayor error.
        """
        original = Image.open(image_path).convert('RGB')
        
        # Re-comprimir a calidad controlada
        import io
        buffer = io.BytesIO()
        original.save(buffer, format='JPEG', quality=self.ELA_QUALITY)
        buffer.seek(0)
        recompressed = Image.open(buffer)
        
        # Diferencia amplificada
        ela_img = np.abs(
            np.array(original, dtype=np.int16) -
            np.array(recompressed, dtype=np.int16)
        ) * self.ELA_SCALE
        
        return float(np.mean(ela_img))   # Score alto = posible edición
    
    def analyze_exif(self, image_path: str) -> dict:
        """Busca software de edición sospechoso en metadatos EXIF."""
        SUSPICIOUS_SOFTWARE = [
            'photoshop', 'gimp', 'paint.net', 'lightroom',
            'affinity', 'pixelmator', 'canva'
        ]
        
        try:
            exif_data = piexif.load(image_path)
            software = exif_data.get('0th', {}).get(piexif.ImageIFD.Software, b'')
            software_str = software.decode('utf-8', errors='ignore').lower()
            
            return {
                'software_detected': software_str,
                'is_suspicious': any(s in software_str for s in SUSPICIOUS_SOFTWARE)
            }
        except Exception:
            return {'software_detected': 'unknown', 'is_suspicious': False}
    
    def predict_fraud(self, image_path: str) -> dict:
        """
        Predicción final de fraude combinando ELA + EXIF + heurísticas.
        """
        ela_score    = self.compute_ela(image_path)
        exif_result  = self.analyze_exif(image_path)
        
        # Heurística: ELA > 8.0 es sospechoso para documentos oficiales
        ela_suspicious  = ela_score > 8.0
        exif_suspicious = exif_result['is_suspicious']
        
        fraud_score = (ela_score / 20.0) + (0.4 if exif_suspicious else 0)
        is_fraud    = ela_suspicious or exif_suspicious
        
        return {
            'is_fraud':        is_fraud,
            'fraud_score':     round(min(fraud_score, 1.0), 4),
            'ela_score':       round(ela_score, 4),
            'exif_suspicious': exif_suspicious,
            'software_found':  exif_result['software_detected']
        }
```

**Rúbrica S5 (20 pts):**

| Criterio | Pts |
|---|---|
| ELA implementado y funcional | 6 |
| Análisis EXIF detecta software sospechoso | 4 |
| XGBoost entrenado con ≥50 muestras sintéticas | 6 |
| Métricas documentadas (F1 ≥ 0.80) | 4 |

---

### Semana 6 — API Segura + Azure Deployment

**Rama:** `feature/s6-secure-api-azure`  
**PR hacia:** `main`

**Entregables:**
- [ ] API FastAPI completa con todos los endpoints
- [ ] Seguridad: JWT, rate limiting, CORS, security headers
- [ ] Azure App Services configurado (westus3)
- [ ] Azure Blob Storage con AES-256 para imágenes
- [ ] Azure Key Vault para SECRET_KEY y connection strings
- [ ] `semana-06/Azure_Deploy.md` — pasos de despliegue reproducibles

**Seguridad de la API:**

```python
# src/api/security.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

def configure_security(app: FastAPI):
    """Aplica todas las capas de seguridad a la API."""
    
    # CORS restrictivo (solo dominio propio)
    app.add_middleware(
        CORSMiddleware,
        allow_origins  = ["https://verifyid.uqaisolutions.com.pe"],
        allow_methods  = ["POST", "GET"],
        allow_headers  = ["Authorization", "Content-Type"],
    )
    
    # Security headers
    @app.middleware("http")
    async def add_security_headers(request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"]     = "nosniff"
        response.headers["X-Frame-Options"]            = "DENY"
        response.headers["Strict-Transport-Security"]  = "max-age=31536000"
        response.headers["Content-Security-Policy"]    = "default-src 'self'"
        return response

# Rate limiting: 5 verificaciones por minuto por IP
@app.post("/api/v1/verify-identity")
@limiter.limit("5/minute")
async def verify_identity(request: Request, ...):
    ...
```

**Rúbrica S6 (20 pts):**

| Criterio | Pts |
|---|---|
| API desplegada en Azure (URL funcional) | 6 |
| JWT funcional con expiración 15 min | 4 |
| Rate limiting configurado y verificado | 4 |
| Security headers presentes (verificar con securityheaders.com) | 3 |
| Azure Key Vault para secrets (no hardcoded) | 3 |

---

### Semana 7 — PenTest por G5 + Hardening

**Rama:** `feature/s7-pentest-hardening`  
**PR hacia:** `main`

**Nota especial:** El Grupo 5 (UQ·AuditAI) auditará este sistema. G6 debe:

**Entregables:**
- [ ] `semana-07/PenTest_Report_G5.md` — reporte de vulnerabilidades encontradas por G5
- [ ] `semana-07/Hardening_Response.md` — correcciones implementadas
- [ ] Pruebas de: SQL injection en campos OCR, path traversal en upload, IDOR en resultados
- [ ] OWASP ZAP scan del endpoint `/verify-identity`
- [ ] Checklist OWASP API Security Top 10 completado

**Checklist de Seguridad Final:**

| Vulnerabilidad OWASP | Estado | Evidencia |
|---|:---:|---|
| API1 — Broken Object Level Authorization | ⬜ | |
| API2 — Broken Authentication (JWT) | ⬜ | |
| API3 — Broken Object Property Auth | ⬜ | |
| API4 — Unrestricted Resource Consumption | ⬜ | Rate limiting |
| API5 — Broken Function Level Auth | ⬜ | |
| API8 — Security Misconfiguration | ⬜ | Security headers |
| A01 — Broken Access Control (IDOR) | ⬜ | |
| A03 — Injection (en datos OCR) | ⬜ | |
| A05 — Security Misconfiguration | ⬜ | |
| A07 — Identification Failures | ⬜ | Liveness + ELA |

**Rúbrica S7 (20 pts):**

| Criterio | Pts |
|---|---|
| Reporte PenTest de G5 recibido e integrado | 6 |
| ≥3 vulnerabilidades corregidas con evidencia | 8 |
| OWASP checklist ≥80% completado | 6 |

---

### Semana 8 ★ — EXPOSICIÓN FINAL (EF) — 100%

**Rama:** `feature/s8-final-demo`  
**PR hacia:** `main`

**Entregables finales:**
- [ ] Sistema completo funcional en `verifyid.uqaisolutions.com.pe`
- [ ] Demo end-to-end: DNI sintético → OCR → Face → Fraud → Resultado
- [ ] `semana-08/Paper_Draft.md` — borrador del artículo Scopus Q1
- [ ] `semana-08/Final_Metrics.md` — métricas de los 3 módulos
- [ ] `semana-08/Slides_EF.pdf` — presentación final

**Demo flow (5 minutos):**
```
1. [0:00] Subir DNI sintético → OCR extrae: DNI, nombre, fechas
2. [1:30] Subir selfie → Face match: similarity = 0.87 ✅
3. [2:30] Subir DNI alterado → Fraud: ela_score=12.3, is_fraud=true ❌
4. [3:30] Subir foto de pantalla (selfie) → Liveness: is_live=false ❌
5. [4:00] Mostrar logs de auditoría en Azure
6. [4:30] Mostrar métricas finales del sistema
```

**Métricas objetivo para publicación Scopus:**

| Módulo | Métrica | Mínimo aceptable | Objetivo |
|---|---|---|---|
| OCR | Accuracy DNI number | 90% | 95% |
| Face | Verification accuracy | 85% | 92% |
| Liveness | Anti-spoofing accuracy | 85% | 90% |
| Fraud | F1-score | 80% | 88% |
| API | Latencia P95 | < 3s | < 1.5s |

**Rúbrica EF (30 pts):**

| Criterio | Pts |
|---|---|
| Demo completo funcional sin errores | 8 |
| Métricas documentadas y reproducibles | 6 |
| Borrador artículo Scopus con abstract, intro, metodología | 8 |
| Presentación oral clara y técnica | 5 |
| Código limpio, documentado y con tests | 3 |

---

## 🗂️ Estructura Completa del Proyecto

```
PS-P6-IdentityVerify-OCR/
├── README.md                          ← Este archivo
├── CONTRIBUTING.md                    ← Guía Fork → Branch → PR
├── LICENSE                            ← MIT License
├── .gitignore
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── ocr/
│   │   ├── __init__.py
│   │   ├── document_scanner.py        ← Tesseract + EasyOCR pipeline
│   │   └── image_preprocessor.py     ← OpenCV preprocessing
│   ├── face_recognition/
│   │   ├── __init__.py
│   │   ├── face_matcher.py            ← DeepFace VGG-Face2
│   │   └── liveness_detector.py      ← Anti-spoofing con OpenCV
│   ├── fraud_detection/
│   │   ├── __init__.py
│   │   ├── fraud_detector.py          ← ELA + EXIF + XGBoost
│   │   └── ela_analyzer.py           ← Error Level Analysis
│   ├── auth/
│   │   ├── __init__.py
│   │   └── jwt_handler.py            ← JWT HS256 + Azure Key Vault
│   └── api/
│       ├── __init__.py
│       ├── main.py                   ← FastAPI application
│       ├── routes.py                 ← Endpoints
│       └── security.py              ← Middlewares de seguridad
│
├── tests/
│   ├── test_ocr.py
│   ├── test_face_matcher.py
│   ├── test_fraud_detector.py
│   ├── test_liveness.py
│   └── test_api_endpoints.py
│
├── docs/
│   ├── architecture.md
│   ├── api-reference.md
│   ├── scopus-guide.md
│   └── threat-model.md
│
├── semana-01/
│   ├── README.md                     ← Entregables S1
│   └── STRIDE_ThreatModel.md
├── semana-02/
│   ├── README.md
│   └── OCR_Results.md
├── semana-03/
│   ├── README.md
│   └── Face_Results.md
├── semana-04/
│   └── README.md                     ← EP Demo + integración
├── semana-05/
│   ├── README.md
│   └── Fraud_Model_Metrics.md
├── semana-06/
│   ├── README.md
│   └── Azure_Deploy.md
├── semana-07/
│   ├── README.md
│   ├── PenTest_Report_G5.md
│   └── Hardening_Response.md
└── semana-08/
    ├── README.md
    ├── Paper_Draft.md
    ├── Final_Metrics.md
    └── Slides_EF.pdf
```

---

## 🔗 Repositorios de Referencia GitHub

### OCR y Procesamiento de Documentos
| Repositorio | Descripción | Link |
|---|---|---|
| **tesseract-ocr/tesseract** | Motor OCR open source más usado del mundo | https://github.com/tesseract-ocr/tesseract |
| **JaidedAI/EasyOCR** | OCR con 80+ idiomas, fácil de integrar | https://github.com/JaidedAI/EasyOCR |
| **madmaze/pytesseract** | Wrapper Python para Tesseract | https://github.com/madmaze/pytesseract |
| **opencv/opencv** | Computer vision, preprocessing de imágenes | https://github.com/opencv/opencv |
| **UB-Mannheim/tesseract** | Tesseract con modelos entrenados en español | https://github.com/UB-Mannheim/tesseract |

### Reconocimiento Facial y Liveness
| Repositorio | Descripción | Link |
|---|---|---|
| **serengil/deepface** | Framework unificado de reconocimiento facial (VGG, ArcFace, FaceNet) | https://github.com/serengil/deepface |
| **ageitgey/face_recognition** | Reconocimiento facial con dlib (99.38% accuracy) | https://github.com/ageitgey/face_recognition |
| **ipazc/mtcnn** | Detección de caras multi-task CNN | https://github.com/ipazc/mtcnn |
| **lindadong/anti-spoofing** | Liveness detection anti-spoofing | https://github.com/lindadong/anti-spoofing |

### Detección de Fraude Documental
| Repositorio | Descripción | Link |
|---|---|---|
| **dmlc/xgboost** | XGBoost para clasificación de fraude | https://github.com/dmlc/xgboost |
| **GuidoBartoli/sherloq** | Análisis forense de imágenes (ELA incluido) | https://github.com/GuidoBartoli/sherloq |
| **haralampiev-ml/ela-fraud-detection** | ELA para detección de manipulación | https://github.com/haralampiev-ml/ela-fraud-detection |

### Seguridad y API
| Repositorio | Descripción | Link |
|---|---|---|
| **tiangolo/fastapi** | Framework REST API de alto rendimiento | https://github.com/tiangolo/fastapi |
| **OWASP/API-Security** | OWASP API Security Top 10 — guía completa | https://github.com/OWASP/API-Security |
| **mpdavis/python-jose** | JWT en Python (HS256, RS256) | https://github.com/mpdavis/python-jose |
| **laurentS/slowapi** | Rate limiting para FastAPI | https://github.com/laurentS/slowapi |

### Proyectos KYC similares de referencia
| Repositorio | Descripción | Link |
|---|---|---|
| **ayushkumar605/KYC-Verification** | Sistema KYC con OCR + face matching | https://github.com/ayushkumar605/KYC-Verification |
| **bhavyagor/Document-Verification** | Verificación de documentos con OpenCV | https://github.com/bhavyagor/Document-Verification |
| **Janmejay-Pandya/KYC-automation** | KYC automatizado con DeepFace | https://github.com/Janmejay-Pandya/KYC-automation |

---

## 🚀 Inicio Rápido

```bash
# 1. Fork del repositorio → clonar tu fork
git clone https://github.com/TU-USUARIO/PS-P6-IdentityVerify-OCR.git
cd PS-P6-IdentityVerify-OCR

# 2. Instalar dependencias del sistema (Ubuntu/Mac)
# Mac: brew install tesseract tesseract-lang-spa
# Ubuntu: sudo apt install tesseract-ocr tesseract-ocr-spa

# 3. Entorno virtual Python
python -m venv venv
source venv/bin/activate          # Mac/Linux
# venv\Scripts\activate           # Windows

# 4. Instalar dependencias Python
pip install -r requirements.txt

# 5. Crear archivo de variables de entorno
cp .env.example .env
# Editar .env con tus credenciales Azure

# 6. Ejecutar API en desarrollo
uvicorn src.api.main:app --reload --port 8000

# 7. Ver documentación interactiva
# http://localhost:8000/docs
```

---

## 🔄 Flujo de Trabajo — Fork → Branch → PR

```
1. Fork del repositorio del curso en tu cuenta GitHub
2. Clonar tu fork localmente
3. Crear rama para cada semana: git checkout -b feature/s1-setup-stride
4. Desarrollar la funcionalidad de la semana
5. Commit con mensaje descriptivo: git commit -m "feat(s1): agregar STRIDE threat model"
6. Push a tu fork: git push origin feature/s1-setup-stride
7. Abrir Pull Request hacia main del repo original
8. El docente revisa y aprueba antes del merge
```

**Convención de commits (Conventional Commits):**
```
feat(s1): nueva funcionalidad de la semana
fix(ocr): corregir extracción de fechas
docs(readme): actualizar métricas
test(face): agregar tests de liveness
security(api): agregar rate limiting
```

---

## 📊 Resumen de Evaluación

| Semana | Entregable | Peso |
|:---:|---|:---:|
| S1 | Setup + STRIDE | 10% |
| S2 | OCR Pipeline | 15% |
| S3 | Face Recognition + Liveness | 15% |
| **S4** | **★ EP — Exposición Parcial** | **20%** |
| S5 | Fraud Detection | 15% |
| S6 | Azure Deploy + API Segura | 10% |
| S7 | PenTest + Hardening | 5% |
| **S8** | **★ EF — Exposición Final** | **10%** |

---

## 📞 Contacto

| Rol | Nombre | Contacto |
|---|---|---|
| Docente / Coautor Scopus | Mg. Ruben Quispe Llacctarimay | rubencarty4@gmail.com |
| Repositorio del curso | DD281-Programacion-Segura-2026-1 | GitHub Classroom |

---

*Universidad Autónoma del Perú — Escuela de Ingeniería de Sistemas — DD281 Programación Segura — Ciclo 2026-1*
*UQ AI SOLUTION COMPANY SAC — G6: UQ·VerifyID*
