from PIL import Image

def encrypt_image(image_path, shift):
    image = Image.open(image_path)
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r + shift) % 256, (g + shift) % 256, (b + shift) % 256

    encrypted_image_path = image_path.replace(".png", "_encrypted.png")
    image.save(encrypted_image_path)
    print(f"Encrypted image saved as {encrypted_image_path}")

def decrypt_image(image_path, shift):
    image = Image.open(image_path)
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r - shift) % 256, (g - shift) % 256, (b - shift) % 256

    decrypted_image_path = image_path.replace("_encrypted.png", ".png")
    image.save(decrypted_image_path)
    print(f"Decrypted image saved as {decrypted_image_path}")

def main():
    image_path = input("Enter the path to the image you want to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypt_image(image_path, shift)

    encrypted_image_path = image_path.replace(".png", "_encrypted.png")
    decrypt_image(encrypted_image_path, shift)

if __name__ == "__main__":
    main()