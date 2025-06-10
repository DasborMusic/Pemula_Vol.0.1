# utils.py
def generate_image(prompt):
    print(f"Menghasilkan gambar dari prompt: {prompt} (simulasi)")
    from PIL import Image, ImageDraw
    img = Image.new("RGB", (512, 512), color="black")
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), prompt, fill="white")
    img.save("output.png")
    print("Gambar berhasil disimpan sebagai output.png")
