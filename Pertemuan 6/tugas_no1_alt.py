# inputan bilangan yang akan dicek
bil = int(input("Masukkan sebuah bilangan: "))

# mendefinisikan fungsi
def hasil(bil):

# algoritma menentukan bilangan ganjil/genap
    if (bil % 2 == 0):
        print("Bilangan yang anda masukkan adalah Genap")
    else:
        print("Bilangan yang anda masukkan adalah Ganjil")

# memanggil fungsi
hasil(bil)

