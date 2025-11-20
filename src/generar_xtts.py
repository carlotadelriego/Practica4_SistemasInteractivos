from TTS.api import TTS
import soundfile as sf

# Texto que quieres que diga el modelo
texto = "Este es un ejemplo generado con el modelo XTTS para la práctica."

# Ruta del fragmento original
audio_referencia = "audio/audio_original.wav"

# Cargar el modelo XTTS v2
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

# Generar el audio zero-shot
audio = tts.tts(
    text=texto,
    speaker_wav=audio_referencia,
    language="es"
)

# Guardar resultado
sf.write("audio/output_xtts.wav", audio, 24000)

print("Audio generado y guardado como audio/output_xtts.wav")
