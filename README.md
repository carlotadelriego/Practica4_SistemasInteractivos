# Práctica 3 — Zero-Shot Voice Cloning (Sistemas Interactivos Inteligentes)

Esta práctica implementa un sistema de clonación de voz *zero-shot* utilizando distintos modelos TTS, y evaluando sus resultados mediante métricas objetivas y análisis subjetivo.  

---

## Estructura del proyecto
PRACTICA4/
│
├── audio/
│ ├── audio_original.wav
│ ├── leyendas_15_becquer.mp3
│ ├── output_xtts.wav
│ ├── output_yourtts.wav
│ └── extraer_snipped.py
│
├── src/
│ ├── generar_xtts.py
│ ├── generar_yourtts.py
│ └── evaluar.py
│
├── Dockerfile
├── Makefile
├── requirements.txt
├── README.md
└── memoria.pdf


---

## Instalación y ejecución con Docker

### 1. Construir la imagen:
bash
make build

### 2. Ejecutar el contenedor:
make run

---

## Generación de audio

Dentro del contenedor
1. Generar con XTTS: python src/generar_xtts.py
2. Generar con YourTTS: python src/generar_yourtts.py

---

## Evaluación de resultados

El script compara audio original con audios clonados mediante: ECAPA-TDNN (SpeechBrain), Resemblyzer (cosine similarity)

Para obtener los resultados de la evaluación se ejecuta: python src/evaluar.py

---

## Dependencias

Están definidas en requirements.txt para ser instaladas automáticamente por Docker.