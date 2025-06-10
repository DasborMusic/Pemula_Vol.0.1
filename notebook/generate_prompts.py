# notebooks/generate_prompts.py
import yaml
from pathlib import Path
from utils import generate_image

def load_prompts(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data['prompts']

if __name__ == "__main__":
    prompts = load_prompts(Path("../configs/heavy_metal_prompts.yaml"))
    for i, prompt in enumerate(prompts, 1):
        print(f"[{i}] Prompt: {prompt}")
        generate_image(prompt, output_path=f"output_{i}.png")
