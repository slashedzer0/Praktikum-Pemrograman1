def addData(listBuah):
    print("Masukkan jumlah buah yang ingin ditambahkan: ")
    totalBuah = input()

    buah = []
    for i in range(totalBuah):
        namaBuah = input(f"Masukkan nama Buah-{i} : ")
        buah.append(namaBuah)
        totalBuah = totalBuah - 1

