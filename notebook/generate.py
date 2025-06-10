# generate.py
from utils import load_model, generate_image

def main():
    prompt = input("Masukkan prompt untuk gambar Heavy Metal: ")
    model = load_model("stable-diffusion")
    result = generate_image(model, prompt)
    result.save("output.png")
    print("Gambar berhasil disimpan sebagai output.png")

if __name__ == "__main__":
    main()
