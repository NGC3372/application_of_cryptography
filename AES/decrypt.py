from Crypto.Cipher import AES

file_key = open('key', 'rb')
key = file_key.read()
file_key.close()

file_encrypt_data = open('encrypted_data', 'rb')
encrypted_data = file_encrypt_data.read()
file_encrypt_data.close()
print(encrypted_data)

cipher = AES.new(key=key, mode=AES.MODE_CFB)
decrypted_data = cipher.decrypt(encrypted_data)
print(bytes.decode(decrypted_data))

