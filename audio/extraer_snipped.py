from pydub import AudioSegment

# Cargar audio completo
audio = AudioSegment.from_mp3("leyendas_15_becquer.mp3")

# Definir segundos que queremos extraer
start_ms = 20 * 1000   # empieza en el segundo 20
end_ms = 30 * 1000     # termina en el segundo 30

snippet = audio[start_ms:end_ms]

# Guardar snippet
snippet.export("audio_original.wav", format="wav")
print("Snippet guardado como audio_original.wav")