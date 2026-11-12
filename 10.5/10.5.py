filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")

while True:
    name = input("\nPlease enter your name: ")
    if name.lower() == 'quit':
        break
    
    print(f"Welcome, {name}! Your visit has been logged.")
    
    # Menggunakan mode 'append' ('a') agar setiap nama baru ditambahkan di baris baru
    with open(filename, 'a') as file_object:
        file_object.write(f"{name}\n")