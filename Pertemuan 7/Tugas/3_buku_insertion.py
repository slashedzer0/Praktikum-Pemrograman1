# algoritma insertion sort secara ascending
def ascending(arrayBuku):
    for i in range(1, len(arrayBuku)):
        item = arrayBuku[i]
        j = i - 1
        while j >= 0 and arrayBuku[j] > item:
            arrayBuku[j + 1] = arrayBuku[j]
            j -= 1
        arrayBuku[j + 1] = item       
    return arrayBuku

# algoritma insertion sort secara descending
def descending(arrayBuku):
    for i in range(1, len(arrayBuku)):
        item = arrayBuku[i]
        j = i - 1
        while j >= 0 and arrayBuku[j] < item:
            arrayBuku[j + 1] = arrayBuku[j]
            j -= 1
        arrayBuku[j + 1] = item       
    return arrayBuku

# menambahkan jumlah dan judul buku
totalBuku = int(input("Masukkan total Buku      : "))
buku = []
for i in range(totalBuku):
    judulBuku = input(f"Masukkan judul Buku ke-{i} : ")
    buku.append(judulBuku)
    totalBuku = totalBuku - 1

# user input
print()
print("<====== Urutkan ? ======>")
print("1. Insertion Ascending")
print("2. Insertion Descending")
pilih = int(input("Pilih    : "))
print()

# output
if pilih == 1:
    ascending(buku)
    print ("Sorting Buku secara Ascending")
    for i in range(len(buku)):
        print(f"Indeks ke-{i} : {buku[i]}")
elif pilih == 2:
    descending(buku)
    print ("Sorting Buku secara Descending")
    for i in range(len(buku)):
        print(f"Indeks ke-{i} : {buku[i]}")
else:
    print("Input tidak valid!")