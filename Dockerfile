# Imagen base con Python 3.10
FROM python:3.10-slim

# Evitar interacciones en la instalación
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsndfile1 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Crear carpeta de trabajo
WORKDIR /app

# Copiar requirements antes para aprovechar cache
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Crear carpetas si no existen
RUN mkdir -p audio

# Comando por defecto (puede cambiarse con make run)
CMD ["bash"]
