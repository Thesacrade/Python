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

#assymetric Encryption using RSA
def rsa_ed(message):
    # Generate RSA keys
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    #Encrypt the message
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ) 
    #Decrypt the message
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    return plaintext.decode(), ciphertext.hex()

if __name__ == "__main__":
    message = "Hello, World!"
    plaintext, ciphertext = rsa_ed(message)
    print("Original Message:", message)
    print("Ciphertext:", ciphertext)
    print("Decrypted Message:", plaintext)