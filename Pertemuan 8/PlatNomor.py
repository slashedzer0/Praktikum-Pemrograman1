def platNomor(plat, nomor):
    print(f"Data: {plat}")

    for i in range(len(plat)):

        if str(plat[i]).upper() == nomor.upper():
            print(f"Nomor kendaraan [{nomor}] ditemukan pada index ke-{i}")
            return i

    print(f"Error! Nomor kendaraan [{nomor}] tidak ditemukan!")
    return -1

plat = ['R 300 SR', 'R 1234 DJ', 'R 701 LP', 'R 3218 RR', 'R 007 TU', 'R 3 ST', 'R 999 RT', 'R 210 RO', 'R 1111 II', 'R 4987 LH']
nomor = input("Masukkan nomor kendaraan yang ingin dicek: ")

platNomor(plat, nomor)
