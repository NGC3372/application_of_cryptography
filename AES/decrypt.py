from Crypto.Cipher import AES
from byte_to_str import str_to_bytes

file_key = open('src/key', 'r')
key = str_to_bytes(file_key.read())
file_key.close()

file_encrypt_data = open('src/encrypted_data', 'r')
encrypted_data_str = file_encrypt_data.read()
file_encrypt_data.close()
encrypted_data = str_to_bytes(encrypted_data_str)

cipher = AES.new(key=key, mode=AES.MODE_CFB, IV=b'1234567890123456')
decrypted_data = cipher.decrypt(encrypted_data)
print(bytes.decode(decrypted_data))

