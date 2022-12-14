# Program menampilkan bilangan genap
bil = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in bil:
    if (n % 2 == 0):
        genap = n
        print(genap)

# Program mencari data pada array
x = int(input("Masukkan jumlah kata: "))
kata = []

for i in range(x):
    kata.append(input("Masukkan kata: "))
    if i == x - 1:
        print("")
        cari = input("Masukkan kata yang ingin dicari: ")
        
        for f in kata:
            if f == cari
                print(f"{cari} ditemukan pada index ke-{kata.index(f)}")
            
            else:
                print("Data tidak ditemukan!")