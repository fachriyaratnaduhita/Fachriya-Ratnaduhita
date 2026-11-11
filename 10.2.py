filename = 'learning_python.txt'

try:
    with open(filename, encoding='utf-8') as file_object:
        lines = file_object.readlines()

    for line in lines:
        # Mengganti kata 'Python' menjadi 'C'
        modified_line = line.replace('Python', 'C')
        print(modified_line.strip())

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found. Please create it first!")