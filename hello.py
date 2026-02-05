import hashlib
""" text = 'Hello World'
hash_object = hashlib.sha256(text.encode())
hex_dig = hash_object.hexdigest()
print(hex_dig)
  """

def hash_file(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()

def check_integrity(filepath1, filepath2):
    print("Checking integrity of the files...")
    hash1 = hash_file(filepath1)
    hash2 = hash_file(filepath2)
    if hash1 == hash2:
        print("The files are identical.")
    else:
        print("The files are different.")

if __name__ == "__main__":
    check_integrity(r"files/sample_text1.txt", r"files/sample_text2.txt")