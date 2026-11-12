print("Give me two numbers, and I will add them.")

# Meminta input dua angka dari pengguna
first_number = input("First number: ")
second_number = input("Second number: ")

try:
    # Mencoba mengonversi input string menjadi integer dan menjumlahkannya
    answer = int(first_number) + int(second_number)
except ValueError:
    # Blok ini dieksekusi jika pengguna memasukkan huruf/teks (bukan angka)
    print("Error: Please enter numbers only, not letters!")
else:
    # Blok ini dieksekusi jika tidak ada error sama sekali
    print(f"The sum of {first_number} and {second_number} is: {answer}")