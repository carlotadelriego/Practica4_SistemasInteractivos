#!/usr/bin/env bash
set -e

echo "=== GPT-SoVITS DOCKER: Iniciando inferencia ==="

python /workspace/sovits_inference.py \
    --ref_path /data/audio/original.wav \
    --text "Hola, esta es una prueba de clonación de voz usando GPT-SoVITS en Docker." \
    --out_path /data/outputs/sovits_output.wav

echo "=== Audio generado en /data/outputs/sovits_output.wav ==="
