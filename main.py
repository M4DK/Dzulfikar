from collections import Counter

print("=== GAME PENGHITUNG KATA ===")
text = input("Masukkan kalimat: ")

# Hitung jumlah karakter
char_count = len(text)

# Hitung jumlah kata
words = text.split()
word_count = len(words)

# Hitung kata paling sering
word_freq = Counter(words)
most_common = word_freq.most_common(1)[0] if word_freq else ("-", 0)

# Tampilkan hasil
print("\n📊 HASIL ANALISIS:")
print(f"Jumlah kata       : {word_count}")
print(f"Jumlah karakter   : {char_count}")
print(f"Kata terbanyak    : '{most_common[0]}' sebanyak {most_common[1]}x")
