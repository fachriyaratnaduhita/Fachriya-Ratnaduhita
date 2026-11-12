# Daftar file yang ingin dibaca oleh program
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\n--- Reading {filename} ---")
    try:
        # Mencoba membuka dan membaca isi file
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
            print(contents.strip())
    except FileNotFoundError:
        # Menangani error jika file tidak ditemukan di direktori
        print(f"Sorry, the file '{filename}' does not exist.")