from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from byte_to_str import  bytes_to_str

data = str.encode(open('src/data', 'r').read(), 'utf-8')

public_key = RSA.import_key(open('src/public_key', 'rb').read())
cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted_data = cipher_rsa.encrypt(data)
encrypted_data_str = bytes_to_str(encrypted_data)


file_encrypt_data = open('src/encrypted_data', 'w')
file_encrypt_data.write(encrypted_data_str)
file_encrypt_data.close()

