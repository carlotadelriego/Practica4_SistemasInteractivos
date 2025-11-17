import soundfile as sf
import argparse
import os
import sys
import numpy as np

sys.path.append("/workspace/gpt-sovits")

from inference.infer_tool import Svc, get_units, infer

parser = argparse.ArgumentParser()
parser.add_argument("--ref_path", type=str, required=True)
parser.add_argument("--text", type=str, required=True)
parser.add_argument("--out_path", type=str, required=True)
args = parser.parse_args()

print("Cargando modelo GPT-SoVITS...")

model_path = "/workspace/gpt-sovits/pretrained/gpt_sovits.pth"
config_path = "/workspace/gpt-sovits/pretrained/config.json"

svc_model = Svc(model_path, config_path)

print("Procesando referencia de voz...")
ref_audio, sr = sf.read(args.ref_path)

print("Generando audio...")
output_audio = svc_model.process(
    text=args.text,
    speaker_wav=args.ref_path,
    sr=sr
)

os.makedirs(os.path.dirname(args.out_path), exist_ok=True)
sf.write(args.out_path, output_audio, sr)

print(f"Audio generado: {args.out_path}")
