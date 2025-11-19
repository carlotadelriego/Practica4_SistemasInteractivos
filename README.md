# Practica4_SistemasInteractivos# Practica4_SistemasInteractivos

## Requisitos
- Mac con chip Apple (M1/M2/M3). Recomendado ejecutar localmente para usar MPS.
- Python 3.11
- ffmpeg instalado (brew install ffmpeg)

## Pasos rápidos (local)
1. Crear entorno e instalar deps: 
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

2. Normalizar audio:
make norm

3. Generar con Bark:
make bark

4. Generar con Tortoise:
make tortoise

5. Evaluar métricas:
make metrics

6. Los resultados se guardan en `outputs/` y las métricas en `outputs/metrics.csv`.

## Notas sobre Mac M3 (MPS)
Los scripts detectan MPS si `torch.backends.mps.is_available()`. Asegúrate de instalar la versión de PyTorch compatible con MPS en tu entorno.

## Docker
Incluido Dockerfile por requisitos de entrega. Ten en cuenta que Docker en macOS no proporciona MPS, por lo que los contenedores serán CPU-only.


