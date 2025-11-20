import torch
import torchaudio
from speechbrain.inference import SpeakerRecognition
from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np

# Rutas
orig = "audio/audio_original.wav"
xtts = "audio/output_xtts.wav"
yourtts = "audio/output_yourtts.wav"

print("\n=== CARGANDO AUDIOS ===")
print("Origen:", orig)
print("XTTS:", xtts)
print("YourTTS:", yourtts)

# ---------------------------
# MÉTRICA 1: ECAPA-TDNN
# ---------------------------
print("\n=== MÉTRICA 1: ECAPA-TDNN (SpeechBrain) ===")

spkrec = SpeakerRecognition.from_hparams(
    source="speechbrain/spkrec-ecapa-voxceleb",
    savedir="tmp_spkrec_eval"
)

def ecapa_similarity(a, b):
    score, _ = spkrec.verify_files(a, b)
    return float(score)

sim_xtts_ecapa = ecapa_similarity(orig, xtts)
sim_your_ecapa = ecapa_similarity(orig, yourtts)

print(f"ECAPA - Similitud Origen vs XTTS:     {sim_xtts_ecapa:.4f}")
print(f"ECAPA - Similitud Origen vs YourTTS: {sim_your_ecapa:.4f}")

# ---------------------------
# MÉTRICA 2: RESEMBLYZER
# ---------------------------
print("\n=== MÉTRICA 2: Resemblyzer (Cosine Similarity) ===")

encoder = VoiceEncoder()

def emb(path):
    wav = preprocess_wav(Path(path))
    return encoder.embed_utterance(wav)

emb_orig = emb(orig)
emb_xtts = emb(xtts)
emb_your = emb(yourtts)

def cosine(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

sim_xtts_res = cosine(emb_orig, emb_xtts)
sim_your_res = cosine(emb_orig, emb_your)

print(f"Resemblyzer - Similitud Origen vs XTTS:     {sim_xtts_res:.4f}")
print(f"Resemblyzer - Similitud Origen vs YourTTS: {sim_your_res:.4f}")

print("\n=== EVALUACIÓN FINAL COMPLETADA ===\n")
