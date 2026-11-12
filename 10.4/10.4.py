filename = 'guest.txt'

# Meminta input nama dari pengguna
guest_name = input("Please enter your name: ")

# Menulis nama ke dalam file guest.txt
with open(filename, 'w') as file_object:
    file_object.write(guest_name)

print(f"Thank you, {guest_name}. Your name has been recorded in {filename}.")