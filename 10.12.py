import json

def get_stored_favorite_number():
    """Mendapatkan angka favorit yang sudah tersimpan, jika ada."""
    filename = 'favorite_number.json'
    try:
        with open(filename, 'r') as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def get_new_favorite_number():
    """Meminta input angka favorit baru dari pengguna dan menyimpannya."""
    favorite_number = input("What is your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number

def show_favorite_number():
    """Menampilkan angka favorit atau meminta yang baru jika belum ada."""
    favorite_number = get_stored_favorite_number()
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}.")
    else:
        favorite_number = get_new_favorite_number()
        print(f"We'll remember that when you come back, {favorite_number}!")

# Menjalankan program utama
show_favorite_number()