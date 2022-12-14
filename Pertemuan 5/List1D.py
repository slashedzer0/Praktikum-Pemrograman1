# Pembuatan list buah
buah = ["Apel", "Jeruk", "Anggur", "Pisang"] 

# Cetak nilai buah cara 1
for i in buah:
    print(i)

# Cetak nilai buah cara 2
print(buah)

print(buah[0])

# Menambah item baru ke list buah
buah.append("Mangga")

# Mengosongkan list buah
buah.clear()

# Menghapus index data tertentu dari list buah
buah.pop(2)
print(buah)

# Menghapus sebuah data tertentu dari list buah
buah.remove("Pisang")

# Membalik urutan
buah.reverse()

# Mengurutkan isi list
buah.sort()