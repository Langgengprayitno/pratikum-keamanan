from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

data_kartu = "41111111111111111|123/27"
data_terenkripsi = cipher.encrypt(data_kartu.encode())
data_terdeskripsi = cipher.decrypt(data_terenkripsi).decode()

print("Kunci Enkripsi :",key.decode())
print("Data Terenkripsi :",data_terenkripsi.decode())
print("Data setelah Deskripsi:", data_terdeskripsi)