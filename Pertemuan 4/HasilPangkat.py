bilangan = int(input("Masukkan bilangan     : "))
pencacah = int(input("Masukkan pencacah     : "))

hasil = bilangan

for i in range(pencacah - 1):
    hasil = hasil * bilangan

print(f"Hasil Pangkat         : {hasil}")