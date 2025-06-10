# generate.py
from utils import generate_image

def main():
    prompt = input("Masukkan prompt untuk gambar Heavy Metal: ")
    generate_image(prompt)

if __name__ == "__main__":
    main()
