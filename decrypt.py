import zlib
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

encrypted = b'|{ENCRYPTED MESSAGE THERE}|'

# private key from keygen.py
private_key = b"""|{KEY THERE}|""" 

rsakey = RSA.importKey(private_key)
rsakey = PKCS1_OAEP.new(rsakey)

chunk_size = 256
offset = 0
decrypted = ""
encrypted = base64.b64decode(encrypted)

while offset < len(encrypted):
    decrypted += str(rsakey.decrypt(encrypted[offset:offset + chunk_size]))
    offset += chunk_size
    
plaintext = zlib.decompress(decrypted)

print(plaintext)