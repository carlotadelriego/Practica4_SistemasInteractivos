from TTS.api import TTS
import soundfile as sf

texto = "Este es un ejemplo generado con YourTTS para la práctica."
audio_referencia = "audio/audio_original.wav"

tts = TTS("tts_models/multilingual/multi-dataset/your_tts")

# language = "en" aunque el texto esté en español
audio = tts.tts(
    text=texto,
    speaker_wav=audio_referencia,
    language="en"
)

sf.write("audio/output_yourtts.wav", audio, 16000)

print("Audio generado: audio/output_yourtts.wav")
