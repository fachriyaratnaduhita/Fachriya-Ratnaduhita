import json

filename = 'favorite_number.json'

try:
    # Mencoba membaca file JSON jika sudah pernah disimpan sebelumnya
    with open(filename, 'r') as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    # Jika file belum ada, minta input dari user lalu simpan
    favorite_number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
        print(f"Thanks! I'll remember that your favorite number is {favorite_number}.")
else:
    # Jika file berhasil ditemukan dan dibaca
    print(f"I know your favorite number! It's {favorite_number}.")