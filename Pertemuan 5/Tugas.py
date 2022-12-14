print("Program Menentukan Predikat Nilai Mata Kuliah")
print()

matkul = int(input("Masukkan jumlah mata kuliah: "))
nilai = []

for i in range(1, matkul + 1):
    nilai.append(float(input(f"Masukkan nilai matkul ke-{i}: ")))
print()

total = sum(nilai)
rata2 = total / matkul

if rata2 > 90 and rata2 <= 100:
    print("Hasil Predikat A dengan nilai: ")
elif rata2 >= 70 and rata2 < 90:
    print("Hasil Predikat B dengan nilai: ")
elif rata2 >= 50 and rata2 < 70:
    print("Hasil Predikat C dengan nilai: ")
elif rata2 >= 30 and rata2 < 50:
    print("Hasil Predikat D dengan nilai: ")
elif rata2 >= 0 and rata2 < 30:
    print("Hasil Predikat E dengan nilai: ")
else:
    print("Nilai tidak valid!")
    exit()

for y in range(1, matkul + 1):
    print(f"Nilai matkul ke-{y}: {nilai[y - 1]}")
print()