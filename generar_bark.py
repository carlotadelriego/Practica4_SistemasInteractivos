from bark import SAMPLE_RATE, generate_audio, preload_models
import soundfile as sf

# Cargar modelos (solo la primera vez tarda)
preload_models()

texto = "Hola, esta es una prueba de Bark generando audio en zero-shot."

audio_array = generate_audio(texto)

# Guardar audio
sf.write("bark_output.wav", audio_array, SAMPLE_RATE)

print("¡Audio generado correctamente!")
