from suno_bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write
import numpy as np

# Pre-carga de modelos
preload_models()

texto = "Este es un ejemplo generado con el modelo Bark para la práctica."
audio_referencia = "audio/audio_original.wav"

# Generar audio con zero-shot
audio = generate_audio(
    texto,
    history_prompt=audio_referencia
)

# Guardar audio
audio_np = np.array(audio)
write("audio/output_bark.wav", SAMPLE_RATE, audio_np)

print("✔ Audio generado y guardado como audio/output_bark.wav")
