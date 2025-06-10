# utils.py
def load_model(model_name):
    print(f"Memuat model: {model_name} (simulasi)")
    return "dummy_model"

def generate_image(model, prompt):
    print(f"Menghasilkan gambar dari prompt: {prompt} (simulasi)")
    from PIL import Image, ImageDraw
    img = Image.new("RGB", (512, 512), color="black")
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), prompt, fill="white")
    img.save(output_path)
    return img
