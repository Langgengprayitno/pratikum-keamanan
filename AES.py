from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

plaintext= "Sabbe Satta Bhavantu Sukhitatta"
key= b'LanggengPrayitno'
data = plaintext.encode('utf-8')
data_padded = pad(data, AES.block_size)

cipher= AES.new(key,AES.MODE_ECB)
ciphertext= cipher.encrypt(data_padded)

cipher_dec= AES.new(key,AES.MODE_ECB)
decrypted= unpad(cipher_dec.decrypt(ciphertext), AES.block_size)

print("Plaintext asli:",plaintext)
print("Ciphertext:",ciphertext.hex())
print("Hasil deskripsi:",decrypted.decode('utf-8'))
