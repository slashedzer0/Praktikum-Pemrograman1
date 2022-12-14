# fungsi menghitung keliling persegi
def keliling(sisi):
    return 4 * sisi

# fungsi menghitung luas persegi
def luas(sisi):
    return sisi * sisi

sisi = int(input("Masukkan sisi persegi: "))
print(f'Keliling persegi     : {keliling(sisi)}')
print(f'Luas persegi         : {luas(sisi)}')