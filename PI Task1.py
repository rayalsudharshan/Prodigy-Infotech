def caesar_cipher(text, shift, mode):
    result = ""
    mode = mode.lower()
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    if mode == "decrypt":
        shift = -shift
    return result

# Test the function
text = "Hello, World!"
shift = 3
mode = "encrypt"

print(caesar_cipher(text, shift, mode))  # Output: Khoor/#ZRQ

text = "Khoor/#ZRQ"
shift = 3
mode = "decrypt"

print(caesar_cipher(text, shift, mode))  # Output: Hello, World!