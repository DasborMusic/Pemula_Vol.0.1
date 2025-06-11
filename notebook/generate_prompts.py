# notebooks/generate_prompts.py
import yaml
from pathlib import Path
import os
from utils import generate_image  # Pastikan utils.py ada di path yang benar

def load_prompts(path: str | Path) -> list[str]:
    """Load prompts from YAML file with error handling."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data.get('prompts', [])
    except (yaml.YAMLError, FileNotFoundError) as e:
        print(f"❌ Error loading prompts: {e}")
        return []

def main():
    # Load prompts
    prompts_path = Path("heavy_metal_prompts.yaml")
    prompts = load_prompts(prompts_path)
    
    if not prompts:
        print("🚫 No valid prompts found. Check your YAML file!")
        return

    # Create output directory
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)

    # Generate images
    for i, prompt in enumerate(prompts, 1):
        print(f"\n🔮 Generating [{i}]: {prompt}")
        
        # Step 1: Generate image (default output.png)
        generate_image(prompt)  # Panggil fungsi lama tanpa output_path
        
        # Step 2: Rename file
        old_path = Path("output.png")
        new_path = output_dir / f"output_{i}.png"
        
        if old_path.exists():
            old_path.rename(new_path)
            print(f"✅ Saved as: {new_path}")
        else:
            print(f"❌ Failed: Default output not found at {old_path}")

if __name__ == "__main__":
    main()
