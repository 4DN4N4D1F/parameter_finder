import base64
import hashlib
from cryptography.fernet import Fernet
import getpass

def get_key(password: str) -> bytes:
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def run_encrypted_py(enc_file):
    password = getpass.getpass("Enter your decryption password: ")
    key = get_key(password)
    fernet = Fernet(key)
    try:
        with open(enc_file, "rb") as f:
            encrypted = f.read()
        decrypted = fernet.decrypt(encrypted)
        code = decrypted.decode()
        exec(code, {"__name__": "__main__"})
    except Exception as e:
        print("Decryption failed or wrong password:", e)

if __name__ == "__main__":
    run_encrypted_py("parameter_finder.py.enc")
