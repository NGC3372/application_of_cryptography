from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from byte_to_str import str_to_bytes

private_key = RSA.import_key(open('src/private_key', 'rb').read())
cipher_rsa = PKCS1_OAEP.new(private_key)

encrypt_data = open('src/encrypted_data', 'r').read()

encrypt_data_byte = str_to_bytes(encrypt_data)
decrypt_data = cipher_rsa.decrypt(encrypt_data_byte)
print(bytes.decode(decrypt_data))


