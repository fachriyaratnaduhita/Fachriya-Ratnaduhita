rivers = ['Nile', 'Amazon', 'Yangtze']
# Indeks maksimal adalah 2, tapi kita memanggil indeks 5 (akan terjadi IndexError)
print(rivers[5])

#CARA MEMPERBAIKI
rivers = ['Nile', 'Amazon', 'Yangtze']
# Memanggil indeks yang valid (misal indeks terakhir -1 atau indeks 2)
print(rivers[2])