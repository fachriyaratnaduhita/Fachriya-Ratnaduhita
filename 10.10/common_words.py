# Exercise 10-10: Common Words
filename = 'siddhartha.txt'

try:
    # Membuka dan membaca seluruh isi file teks
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    # Menangani error jika file teks belum ada di folder
    print(f"Sorry, the file '{filename}' does not exist.")
else:
    # Menghitung kemunculan kata 'the' 
    # Menggunakan .lower() agar pencarian tidak case-sensitive (huruf besar/kecil dihitung semua)
    word_count = contents.lower().count('the')
    
    print(f"The word 'the' appears approximately {word_count} times in '{filename}'.")