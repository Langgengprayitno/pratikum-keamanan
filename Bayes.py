import pandas as pd
import matplotlib.pyplot as plt

# Data dummy
data = {
    "Media": [
        "Acara di sekolah", "Baliho", "Banner", "Brosur", "Iklan Radio",
        "Informasi Teman", "Internet", "Koran", "Pamflet", "Saudara", "Spanduk"
    ],
    "Frekuensi Total (X1)": [117, 124, 90, 256, 87, 350, 64, 49, 70, 99, 190],
    "Frekuensi di Kota A (X2)": [58, 56, 47, 115, 36, 177, 27, 25, 37, 53, 92]
}

# Buat DataFrame
df = pd.DataFrame(data)

# Hitung total frekuensi di Kota A
total_kota_A = df["Frekuensi di Kota A (X2)"].sum()

# Hitung probabilitas
df["Probabilitas di Kota A"] = df["Frekuensi di Kota A (X2)"] / total_kota_A
df["Probabilitas (%)"] = df["Probabilitas di Kota A"] * 100

# Urutkan dari probabilitas tertinggi ke terendah
df_sorted = df.sort_values(by="Probabilitas di Kota A", ascending=False).reset_index(drop=True)

# Tampilkan tabel
print("Probabilitas media promosi di Kota A (urut dari yang paling efektif):\n")
print(df_sorted[["Media", "Frekuensi di Kota A (X2)", "Probabilitas di Kota A", "Probabilitas (%)"]])

# Visualisasi Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(df_sorted["Media"], df_sorted["Probabilitas (%)"], color='skyblue')
plt.title("Probabilitas Media Promosi di Kota A (%) - Bar Chart")
plt.xlabel("Media Promosi")--
plt.ylabel("Probabilitas (%)")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Visualisasi Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(
    df_sorted["Probabilitas di Kota A"],
    labels=df_sorted["Media"],
    autopct='%1.1f%%',
    startangle=140,
    colors=plt.cm.Paired.colors
)
plt.title("Probabilitas Media Promosi di Kota A (%) - Pie Chart")
plt.axis('equal')  # Agar pie chart berbentuk lingkaran
plt.show()

