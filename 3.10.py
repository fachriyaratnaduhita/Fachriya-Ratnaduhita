fruits = ['mango', 'banana', 'apple', 'durian', 'pineapple']

# menuliskan isi list dengan indeksnya
print(fruits[2])

# menuliskan isi list dengan indeks dan juga huruf awal berupa kapital
print(fruits[1].title())

# menuliskan isi list dengan indeks yang berkebalikan
print(fruits[-3])

# membuat pesan untuk sebuah value yang terdapat pada list melalui indeks dan menggunakan huruf kapital di awal kata
message = f"I like {fruits[0].title()}"
print(message)

# mengubah elemen yang terdapat dalam list
fruits = ['mango', 'banana', 'apple', 'durian', 'pineapple']
print(fruits)
fruits[0] = 'watermelon'
print(fruits)

# menambahkan elemen dalam lisy dengan .append()
fruits = ['mango', 'banana', 'apple', 'durian', 'pineapple']
print(fruits)
fruits.append('orange')
print(fruits)

# menambahkan elemen dalam list dengan .insert()
fruits = ['mango', 'banana', 'apple', 'durian', 'pineapple']
fruits.insert(1, 'avocado')
print(fruits)

# menghapus item dari list menggunakan del statement jika mengetahui posisi atau indeks dari item
fruits = ['mango', 'banana', 'apple', 'durian', 'pineapple']
print(fruits)
del fruits[2]
print(fruits)

# mwnggunakan item di list yang sudah dihapus dengan menggunakan .pop()
fruits = ['mango', 'banana', 'apple', 'durian', 'pineapple']
print(fruits)

popped_fruits = fruits.pop()
print(fruits)
print(popped_fruits)

# menggunakan item di list yang sudah dihapus dengan menggunakan .pop() dan dengan menuliskan indeks atau posisi dari elemen tersebut
fruits = ['mango', 'banana', 'apple', 'durian', 'pineapple']
like_fruit = fruits[2]
print(f"I like {like_fruit} so much!")

# menghapus item di list namun tidak mengetahui posisi item tersebut dengan menggunakan .remove()
fruits = ['mango', 'banana', 'apple', 'durian', 'pineapple']
print(fruits)

fruits.remove('banana')
print(fruits)

# mengubah susunan list secara permanen berdasarkan urutan alfabet dengan menggunakan .sort()
fruits = ['mango', 'banana', 'apple', 'durian', 'pineapple']
fruits.sort()
print(fruits)

# mengubah susunan list secara tidak permanen berdasarkan urutan alfabet dengan menggunakan .sorted()
fruits = ['mango', 'banana', 'apple', 'durian', 'pineapple']
print("\nHere is the original list:")
print(fruits)

print("\nHere is the sorted list:")
print(sorted(fruits))

print("\nHere is the original list again:")
print(fruits)

# mengubah susunan list berupa susunan terbalik menggunakan .reverse()
fruits = ['mango', 'banana', 'apple', 'durian', 'pineapple']
print(fruits)

fruits.reverse()
print(fruits)

# menemukan jumlah data dalam list
fruits = ['mango', 'banana', 'apple', 'durian', 'pineapple']
print(len(fruits))