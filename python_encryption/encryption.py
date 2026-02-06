import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Symmetric Encryption using AES-GCM    
def aes_ed(message):
    key = secrets.token_bytes(32)
    nonce = secrets.token_bytes(12)
    aesgcm = AESGCM(key)
    ciphertext = nonce + aesgcm.encrypt(nonce, message.encode(), None)
    plaintext = aesgcm.decrypt(ciphertext[:12], ciphertext[12:], None)
    return key.hex(), plaintext.decode(), ciphertext.hex()

if __name__ == "__main__":
    message = "Hello, World!"
    key, plaintext, ciphertext = aes_ed(message)
    print("Original Message:", message)
    print("Ciphertext:", ciphertext)
    print("Decryption Key:", key)
    print("Decrypted Message:", plaintext)