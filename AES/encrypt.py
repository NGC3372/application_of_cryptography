from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from byte_to_str import bytes_to_str


data = str.encode(open('src/data', 'r').read(), 'utf-8')
key = get_random_bytes(16)
key_str = bytes_to_str(key)
file_key = open('src/key', 'w')
file_key.write(key_str)
file_key.close()

cipher = AES.new(key=key, mode=AES.MODE_CFB, IV=b'1234567890123456')
encrypted_data = cipher.encrypt(data)
encrypted_data_str = bytes_to_str(encrypted_data)

file_encrypt_data = open('src/encrypted_data', 'w')
file_encrypt_data.write(encrypted_data_str)
file_encrypt_data.close()
