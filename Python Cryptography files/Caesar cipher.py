#Programmer: Nafiul Haque
#Date:19/06/2024
#Program: The Caesar Cipher in Cryptography

def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]

        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char

    return result


def main():
    choice = input("Type 'encrypt' to encrypt, 'decrypt' to decrypt: ").lower()
    text = input("Enter your message: ")
    shift = int(input("Enter the shift number: "))

    if choice == 'encrypt':
        print("Encrypted message: " + encrypt(text, shift))
    elif choice == 'decrypt':
        print("Decrypted message: " + decrypt(text, shift))
    else:
        print("Invalid choice! Please choose either 'encrypt' or 'decrypt'.")


if __name__ == "__main__":
    main()
