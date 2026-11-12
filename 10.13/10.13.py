import json

def get_stored_username():
    """Mendapatkan username yang sudah tersimpan jika ada."""
    filename = 'username.json'
    try:
        with open(filename, 'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Meminta input username baru dari pengguna."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Menyapa pengguna dan memverifikasi apakah identitasnya benar."""
    username = get_stored_username()
    
    if username:
        # Memverifikasi apakah nama yang tersimpan sudah benar
        correct = input(f"Are you {username}? (y/n): ")
        if correct.lower() == 'y':
            print(f"Welcome back, {username}!")
            return
            
    # Jika file belum ada atau pengguna menjawab 'n' (nama salah)
    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")

# Menjalankan program utama
greet_user()