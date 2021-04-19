from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


data = str.encode('12345678901234561234567890123456', 'utf-8')
key = get_random_bytes(16)
file_key = open('key', 'wb')
file_key.write(key)
file_key.close()

cipher = AES.new(key=key, mode=AES.MODE_CFB, IV=b'1234567890123456')
encrypted_data = cipher.encrypt(data)

file_encrypt_data = open('encrypted_data', 'wb')
file_encrypt_data.write(encrypted_data)
file_encrypt_data.close()

print(encrypted_data)
print(AES.new(key=key, mode=AES.MODE_CFB, IV=b'1234567890123456').decrypt(encrypted_data))
