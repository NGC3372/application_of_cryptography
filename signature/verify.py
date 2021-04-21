from Crypto.Signature import pss
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from byte_to_str import str_to_bytes

key = RSA.import_key(open('../RSA/src/public_key').read())

data_file = open('src/data', 'r')
data = data_file.read()
data_file.close()

signed_data_file = open('src/signed_data', 'r')
signed_data = signed_data_file.read()
signed_data_file.close()
signed_data_byte = str_to_bytes(signed_data)

h = SHA256.new(str.encode(data))
verifier = pss.new(key)

try:
    verifier.verify(h, signed_data_byte)
    print('YES')
except (ValueError, TypeError):
    print('NO')
