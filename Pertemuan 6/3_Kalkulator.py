print("         KALKULATOR\n")

# fungsi operasi penjumlahan
def jumlah(x, y):
    return x + y

# fungsi operasi perkalian
def kali(x, y):
    return x * y

# fungsi operasi pembagian
def bagi(x, y):
    return x / y

# fungsi operasi pengurangan
def kurang(x, y):
    return x - y

# fungsi operasi perpangkatan
def pangkat(x, y):
    return x ** y

# inputan operasi bilangan yang akan dipilih
print("1. Penjumlahan")
print("2. Perkalian")
print("3. Pembagian")
print("4. Pengurangan")
print("5. Perpangkatan")

pilihan = input("\nMasukkan pilihan   : ")
print()

bil1 = int(input("Bilangan pertama   : "))
bil2 = int(input("Bilangan kedua     : "))

# output
if pilihan == '1':
    print(f"Hasil Penjumlahan  : {jumlah(bil1, bil2)}")
elif pilihan == '2':
    print(f"Hasil Perkalian    : {kali(bil1, bil2)}")
elif pilihan == '3':
    print(f"Hasil Pembagian    : {bagi(bil1, bil2)}")
elif pilihan == '4':
    print(f"Hasil Pengurangan  : {kurang(bil1, bil2)}")
elif pilihan == '5':
    print(f"Hasil Perpangkatan : {pangkat(bil1, bil2)}")
else:
    print("Input tidak valid!")