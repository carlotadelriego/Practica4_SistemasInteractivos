FROM python:3.10-slim

# Dependencias del sistema
RUN apt-get update && apt-get install -y git ffmpeg build-essential wget && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Clonar GPT-SoVITS (solo inference)
RUN git clone https://github.com/RVC-Borus/GPT-SoVITS.git /workspace/gpt-sovits

WORKDIR /workspace/gpt-sovits

# Instalar dependencias
RUN pip install --no-cache-dir torch torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir soundfile librosa numpy

# Copiar script de inferencia y entrypoint
COPY sovits_inference.py /workspace/sovits_inference.py
COPY entrypoint_sovits.sh /workspace/entrypoint_sovits.sh

RUN chmod +x /workspace/entrypoint_sovits.sh

CMD ["/workspace/entrypoint_sovits.sh"]
