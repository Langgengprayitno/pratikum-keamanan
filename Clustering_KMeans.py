import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# Load data
try:
    df = pd.read_csv('D:/Kelompok4_NIM.csv', encoding='latin1')
    tweets = df['Isi Tweet'].dropna().tolist()
except Exception as e:
    print("Gagal membaca file CSV:", e)
    tweets = []

# Preprocessing ringan + hapus stopword Indonesia
factory = StopWordRemoverFactory()
stop_words = set(factory.get_stop_words())

def preprocess(text):
    # Hapus link dan simbol, ubah ke lowercase, tokenisasi, hapus stopword
    text = re.sub(r"http\S+", "", text)               # Hapus URL/link
    text = re.sub(r"[^a-zA-Z\s]", "", text)           # Hapus karakter non-huruf
    text = text.lower()                               # Lowercase
    tokens = text.split()                             # Tokenisasi
    return ' '.join([w for w in tokens if w not in stop_words])  # Hapus stopword

# Terapkan preprocessing ke semua tweet
tweets_cleaned = [preprocess(t) for t in tweets]

# Vectorisasi teks menggunakan TF-IDF
vectorizer = TfidfVectorizer(max_df=0.8, min_df=2)
X = vectorizer.fit_transform(tweets_cleaned)

# Clustering menggunakan KMeans
k = 7
model = KMeans(n_clusters=k, random_state=42, n_init='auto')
model.fit(X)

# Tampilkan hasil clustering
for i in range(k):
    print(f"\nCluster {i+1}:")
    indices = [j for j, label in enumerate(model.labels_) if label == i]
    for idx in indices[:5]:  # Tampilkan 5 tweet pertama dari cluster ini
        print(f"- {tweets[idx]}")
