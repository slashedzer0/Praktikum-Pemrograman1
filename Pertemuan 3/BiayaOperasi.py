print("<-- Menu Hitung Biaya Operasi -->\n")

print("1. Hitung Biaya Operasi Mata")
print("2. Hitung Biaya Operasi Jantung")

operasi = input("\nMasukkan Pilihan: ")

if (operasi == "1"):
    print("JENIS PENYAKIT MATA: \n")
    print("1. Katarak")
    print("2. Plus/Minus")
    print("3. Silinder")

    penyakit_mata = input("\nMasukkan jenis penyakit mata: ")

    if (penyakit_mata == "1"):
        print("Biaya Operasi Mata Katarak = Rp. 7.500.000")
        
    elif (penyakit_mata == "2"):
        print("Biaya Operasi Mata Plus/Minus = Rp. 5.000.000")

    elif (penyakit_mata == "3"):
        print("Biaya Operasi Mata Silinder = Rp. 4.000.000")
    
    else:
        print("Input tidak sesuai!")


elif (operasi == "2"):
    print("JENIS PENYAKIT JANTUNG: \n")
    print("1. Jantung Koroner")
    print("2. Katup Jantung")
    print("3. Otot Jantung")

    penyakit_jantung = input("\nMasukkan jenis penyakit jantung: ")

    if (penyakit_jantung == "1"):
        print("Biaya Operasi Jantung Koroner = Rp. 500.000.000")
    
    elif (penyakit_jantung == "2"):
        print("Biaya Operasi Katup Jantung = Rp. 350.000.000")

    elif (penyakit_jantung == "3"):
        print("Biaya Operasi Otot Jantung = Rp. 450.000.000")

    else:
        print("Input tidak sesuai!")


else:
    print("Pilihan tidak ada!")