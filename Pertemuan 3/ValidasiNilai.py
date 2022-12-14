print("Program Validasi Nilai")

nol = 0

x = float(input("Masukkan bilangan yang akan dibagi: "))
pembagi = int(input("Masukkan bilangan pembagi: "))

if (pembagi == nol):
    print("Pembagi tidak boleh 0!")

else:
    print(f"Hasil bagi: {x / pembagi}")