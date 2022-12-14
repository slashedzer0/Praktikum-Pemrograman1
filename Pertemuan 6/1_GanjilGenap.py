# fungsi menentukan bilangan genap
def genap(bil):
    return bil % 2 == 0

# inputan bilangan yang akan dicek
bil = int(input("Masukkan sebuah bilangan: "))

# output
if genap(bil) == True:
    print("Bilangan yang anda masukkan adalah Genap")
else:
    print("Bilangan yang anda masukkan adalah Ganjil")
