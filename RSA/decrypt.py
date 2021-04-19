from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

private_key = RSA.import_key(open('private_key', 'rb').read())
cipher_rsa = PKCS1_OAEP.new(private_key)

encrypt_data = open('encrypted_data', 'rb').read()

decrypt_data = cipher_rsa.decrypt(encrypt_data)
print(bytes.decode(decrypt_data))


