from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

data = 'hello world!!!!!'.encode('utf-8')

public_key = RSA.import_key(open('public_key', 'rb').read())
cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted_data = cipher_rsa.encrypt(data)

file_encrypt_data = open('encrypted_data', 'wb')
file_encrypt_data.write(encrypted_data)
file_encrypt_data.close()

