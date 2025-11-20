import torchaudio
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio

# Instancia del modelo
tts = TextToSpeech()

texto = "Este es un ejemplo generado con el modelo Tortoise TTS para la práctica."
audio_referencia = "audio/audio_original.wav"

# Cargar referencia (convertida a 22.050 Hz)
ref_audio = load_audio(audio_referencia, 22050)

# Generar voz clonada
generated = tts.tts_with_preset(
    text=texto,
    voice_samples=[ref_audio],
    preset="fast",
)

# Guardar salida con torchaudio
torchaudio.save(
    "audio/output_tortoise.wav",
    generated.squeeze(0).cpu(),
    22050
)

print("Audio generado y guardado como audio/output_tortoise.wav")
