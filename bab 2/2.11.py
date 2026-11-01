my_name = ' Faya '
print("\n\t' Faya '")
#\n itu digunakan untuk meletakkan teks di baris yang baru
#sedangkan \t digunakan untuk menambahkan tab atau menjorokkan teks yang kita buat

my_nameRstrip = my_name.rstrip()
print(f"'{my_nameRstrip}'")
#rstrip berguna untuk menghapus spasi di sebelah kanan dari teks yang kita buat
#f disini adalah format, yang berfungsi untuk menggabungkan antara variabel yang sudah kita buat sebelumnya dengan elemen yang baru yang ingin ditambahkan ketika proses print
#{} berfungsi untuk memanggil isi atau nilai dari variabel yang ada di dalam kurung tersebut

my_nameLstrip = my_name.lstrip()
print(f"'{my_nameLstrip}'")
#lstrip berguna untuk menghapus spasi di sebelah kiri dari teks yang kita buat

my_nameStrip = my_name.strip()
print(f"'{my_nameStrip}'")
#strip berguna untuk menghapus spasi di sebelah kanan dan kiri dari teks yang kita buat