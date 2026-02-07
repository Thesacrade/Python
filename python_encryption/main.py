from password_protection import check_password_strength, hash_password, verify_password     
from hash import hash_file, check_integrity
from encryption import rsa_ed, aes_ed
from getpass import getpass

print("Welcome to this Encryption command line tool!")
def main():
    while True:
        print("\nPlease select an option:")
        print("1. Check Password Strength")
        print("2. Hash a File")
        print("3. Check File Integrity")
        print("4. Symmetric Encryption (AES-GCM)")
        print("5. Asymmetric Encryption (RSA)")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            password = getpass("Enter a password to check its strength: ")
            check_password_strength(password)
            """ hashed_password = hash_password(password)
            print(verify_password(password, hashed_password)) """
        
        elif choice == '2':
            filepath = input("Enter the file path to hash: ")
            print("File Hash:", hash_file(filepath))
        
        elif choice == '3':
            filepath1 = input("Enter the first file path: ")
            filepath2 = input("Enter the second file path: ")
            check_integrity(filepath1, filepath2)
        
        elif choice == '4':
            message = input("Enter a message to encrypt using AES-GCM: ")
            key, plaintext, ciphertext = aes_ed(message)
            print("Original Message:", message)
            print("Ciphertext:", ciphertext)
            print("Decryption Key:", key)
            print("Decrypted Message:", plaintext)

        elif choice == '5':
            message = input("Enter a message to encrypt using RSA: ")
            plaintext, ciphertext = rsa_ed(message)
            print("Original Message:", message)
            print("Ciphertext:", ciphertext)
            print("Decrypted Message:", plaintext)

        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")      
if __name__ == "__main__":
    main()