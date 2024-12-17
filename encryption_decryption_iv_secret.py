import os
import base64

def generate_key(length):
    key_bytes = os.urandom(length)
    return base64.b64encode(key_bytes).decode('utf-8')

secret_key = generate_key(32)
print("SECRET_KEY:", secret_key)

init_vector = os.urandom(16) 
init_vector_b64 = base64.b64encode(init_vector).decode('utf-8')
print("INIT_VECTOR:", init_vector_b64)
