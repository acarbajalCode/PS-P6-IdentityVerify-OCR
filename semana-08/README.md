# Semana 8 ★ — EXPOSICIÓN FINAL (EF) — 100%

**Rama:** `feature/s8-final-demo` → PR hacia `main`

## Entregables finales
- [ ] Sistema completo desplegado en Azure (URL pública)
- [ ] `Paper_Draft.md` — borrador artículo Scopus Q1
- [ ] `Final_Metrics.md` — métricas de los 4 módulos
- [ ] `Slides_EF.pdf` — presentación 10 minutos
- [ ] Video demo de 3 minutos (subir a YouTube unlisted)

## Final_Metrics.md (completar con mediciones reales)

### Módulo OCR
| Campo | Accuracy | Dataset |
|---|---|---|
| DNI number | % | 100 imágenes |
| Fechas | % | 100 imágenes |

### Módulo Face Matching (Ensemble 3 modelos)
| Escenario | Resultado | Accuracy |
|---|---|---|
| Misma persona | similarity ≥ 0.80 | /50 = % |
| Personas distintas | similarity < 0.80 | /50 = % |

### Módulo Liveness Detection
| Ataque | Detectado | Accuracy |
|---|---|---|
| Foto impresa | /30 | % |
| Foto en pantalla | /30 | % |
| Persona real (no bloquear) | /30 | % |

### Módulo Fraud Detection
| Documento | Correcto | Accuracy |
|---|---|---|
| Auténtico (no fraude) | /50 | % |
| Alterado (fraude) | /50 | % |
| F1-Score final | | % |

### Performance API
| Métrica | Valor |
|---|---|
| Latencia promedio | ms |
| Latencia P95 | ms |
| Throughput (req/min) | |

## Paper_Draft.md — Estructura del Artículo Scopus

**Título:**
"FaceDocVerify: A Multi-Modal Secure Identity Verification Framework Integrating Open-Source OCR and Deep Learning Facial Recognition with Real-Time Fraud Detection for Digital Onboarding Processes"

**Abstract (completar ~250 palabras):**
Identity fraud in digital onboarding processes represents a critical challenge for financial and governmental institutions in emerging economies...

**Secciones requeridas:**
1. Introduction
2. Related Work
3. Proposed System Architecture
4. Implementation (OCR + Face + Fraud modules)
5. Experimental Results
6. Security Analysis (STRIDE, PenTest results)
7. Conclusion and Future Work
8. References (IEEE format, ≥20 referencias)
