from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Use EXACTLY 16, 24, or 32 bytes for AES key
KEY = b'supersecretkey12' # 16 bits
IV = b'initialvector123' # 16 bits

def encrypt(plaintext):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    padded_data = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_data)
    return base64.b64encode(ciphertext).decode()

def decrypt(ciphertext):
    try:
        cipher = AES.new(KEY, AES.MODE_CBC, IV)
        decrypted_data = cipher.decrypt(base64.b64decode(ciphertext))
        return unpad(decrypted_data, AES.block_size).decode()  # Remove padding
    except Exception as e:
        return f"Decryption Error: {str(e)}"

