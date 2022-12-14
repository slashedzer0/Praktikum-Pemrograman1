total = 0
x = int(input("Masukkan bilangan: "))

print("Total nilai =", end = " ")

for i in range(x, 0, -1):
    print(i, end = " ")

    if i != 1:
        print("+", end = " ")

    else:
        print("=", end = " ")
    total = total + i

print(total)