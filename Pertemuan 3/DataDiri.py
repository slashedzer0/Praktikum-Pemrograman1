print("==========INPUT==========")

nama = input("Masukkan Nama: ")
gender = input("Jenis Kelamin (L/P): ")
agama = int(input("Masukkan Agama (1~5): "))

if (agama == 1):
    agama = "Islam"

elif (agama == 2):
    agama = "Protestan"

elif (agama == 3):
    agama = "Katolik"

elif (agama == 4):
    agama = "Hindu"
    
elif (agama == 5):
    agama = "Protestan"

else:
    agama = "Agama tidak ditemukan!"

print("==========OUTPUT=========")
print(f"Nama    : {nama.capitalize()}")
print(f"Kelamin : {gender.upper()}")
print(f"Agama   : {agama}")