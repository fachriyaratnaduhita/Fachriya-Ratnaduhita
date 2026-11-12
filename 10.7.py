filename = 'guest_book.txt'

print("Enter 'quit' at any time to stop.")

while True:
    name = input("\nEnter your name: ")
    if name.lower() == 'quit':
        break
    
    try:
        # Membuka file dalam mode append ('a') untuk mencatat nama tamu secara berulang
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"{name}\n")
    except FileNotFoundError:
        # Menangani error jika direktori atau file bermasalah
        print(f"Sorry, the file {filename} cannot be found.")
    else:
        print(f"Hi {name}, your name has been added to {filename}!")