# Daftar file yang ingin dibaca (termasuk file 'rabbits.txt' yang sengaja tidak ada)
filenames = ['cats.txt', 'dogs.txt', 'rabbits.txt']

for filename in filenames:
    try:
        # Mencoba membuka dan membaca file
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # Gagal secara senyap (fail silently) menggunakan pass
        pass
    else:
        # Dijalankan hanya jika file berhasil ditemukan dan dibaca
        print(f"\n--- Reading {filename} ---")
        print(contents.strip())