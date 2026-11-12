import json

def get_stored_username():
    """Mendapatkan username yang tersimpan jika file-nya ada."""
    filename = 'username.json'
    try:
        with open(filename, 'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Meminta input username baru dari pengguna dan menyimpannya ke file JSON."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Menyapa pengguna dengan memverifikasi identitas mereka."""
    username = get_stored_username()
    
    if username:
        # Memverifikasi apakah pengguna saat ini adalah orang yang sama
        confirm = input(f"Are you {username}? (y/n): ")
        if confirm.lower() == 'y':
            print(f"Welcome back, {username}!")
            return

    # Jika file belum ada atau pengguna menjawab 'n' (bukan orang yang sama)
    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")

# Menjalankan program utama
greet_user()