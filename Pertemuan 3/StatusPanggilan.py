gender = input("Perempuan atau Laki-laki? (P/L): ")
status = input("Menikah atau lajang? (Y/N): ")

if gender.upper() == "P" and status.upper() == "N":
    print("Halo, Mbak!")

elif gender.upper() == "L" and status.upper() == "N":
    print("Halo, Mas!")

elif gender.upper() == "P" and status.upper() == "Y":
    print("Halo, Bu!")

elif gender.upper() == "L" and status.upper() == "Y":
    print("Halo, Pak!")

else:
    print("Input tidak sesuai.")