#Programmer: Nafiul Haque
#Date:19/06/2024
#Program: XOR Process - Cryptography with Python

def xor_encrypt_decrypt(message, key):
    # Make sure the key length matches the message length
    key = (key * (len(message) // len(key) + 1))[:len(message)]

    # Perform XOR operation between the message and the key
    encrypted_decrypted_message = ''.join(chr(ord(m) ^ ord(k)) for m, k in zip(message, key))

    return encrypted_decrypted_message

def main():
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
    message = input("Enter the message: ")
    key = input("Enter the key: ")

    result = xor_encrypt_decrypt(message, key)

    if choice == 'encrypt':
        # Display the encrypted message in a readable format (hex)
        print(f"Encrypted message: {result.encode().hex()}")
    elif choice == 'decrypt':
        # If decrypting, assume the input is hex-encoded
        message = bytes.fromhex(message).decode()
        result = xor_encrypt_decrypt(message, key)
        print(f"Decrypted message: {result}")
    else:
        print("Invalid choice. Please type 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
