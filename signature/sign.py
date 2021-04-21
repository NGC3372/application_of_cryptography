from Crypto.Signature import pss
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from byte_to_str import bytes_to_str


data_file = open('src/data', 'r')
data = data_file.read()
data_file.close()

h = SHA256.new(str.encode(data))

key = RSA.import_key(open('../RSA/src/private_key').read())
sign_result = pss.new(key).sign(h)

file = open('src/signed_data', 'w')
file.write(bytes_to_str(sign_result))
file.close()
