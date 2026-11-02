locations = ['Japan', 'Swiss', 'Singapore', 'Canada', 'Malaysia']

# Cetak list dalam urutan asli
print("Here is the original list:")
print(locations)

# Cetak menggunakan sorted() tanpa mengubah list asli
print("\nHere is sorted list:")
print(sorted(locations))

# Buktikan list masih dalam urutan asli
print("\nHere is the original list again:")
print(locations)

# Cetak menggunakan sorted() dengan reverse=True
print("\nHere is the sorted with reverse list:")
print(sorted(locations, reverse=True))

# Buktikan list masih dalam urutan asli
print("\nHere is the original list again:")
print(locations)

# Gunakan reverse() untuk mengubah urutan list
locations.reverse()
print("\nHere is the reverse list:")
print(locations)

# Gunakan reverse() sekali lagi untuk mengembalikan ke posisi semula
locations.reverse()
print("\nHere is the original list again:")
print(locations)

# Gunakan sort() untuk mengubah secara permanen menjadi alfabetis
locations.sort()
print("\nHere is the sort list:")
print(locations)

# Gunakan sort() dengan reverse=True secara permanen
locations.sort(reverse=True)
print("\nHere is the sort with reverse list:")
print(locations)