x = int(input("Masukkan bilangan pertama: "))
y = int(input("Masukkan bilangan kedua  : "))

kpk = x

while (kpk % y != 0):
       kpk = kpk + x

print(f"KPK: {kpk}")