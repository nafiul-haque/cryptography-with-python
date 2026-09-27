#Programmer: Nafiul Haque
#Date:19/06/2024
#Program: Implementing Reverse Cipher in Cryptography (Reverse Cipher for encrypt a decrypted message)

def reverse_cipher_encrypt(decrypted_message):
    # Reverse the decrypted message to encrypt it
    encrypted_message = decrypted_message[::-1]
    return encrypted_message


def main():
    # Ask the user for a decrypted message
    decrypted_message = input("Enter the decrypted message: ")

    # Encrypt the message
    encrypted_message = reverse_cipher_encrypt(decrypted_message)
    print(f"Encrypted message: {encrypted_message}")


if __name__ == "__main__":
    main()


