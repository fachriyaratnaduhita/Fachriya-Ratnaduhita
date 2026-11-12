filename = 'learning_python.txt'

try:
    # 1. Membaca seluruh file sekaligus
    print("--- Reading the entire file ---")
    with open(filename, encoding='utf-8') as file_object:
        contents = file_object.read()
        print(contents)

    # 2. Membaca baris per baris dengan looping
    print("\n--- Looping over the file object ---")
    with open(filename, encoding='utf-8') as file_object:
        for line in file_object:
            print(line.strip())

    # 3. Menyimpan baris ke dalam list
    print("\n--- Storing lines in a list ---")
    with open(filename, encoding='utf-8') as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.strip())

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found. Please create it first!")
