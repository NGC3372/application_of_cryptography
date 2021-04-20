from Crypto.PublicKey import RSA


key = RSA.generate(2048)
file_private = open('src/private_key', 'wb')
file_private.write(key.export_key())
file_private.close()

file_public = open('src/public_key', 'wb')
file_public.write(key.publickey().export_key())
file_public.close()
