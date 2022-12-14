temp = int(input("Masukkan besarnya suhu: "))

if (temp <= 0):
    print(f"Pada suhu {temp}°C, air akan membeku.")

elif (temp > 0 and temp < 100):
    print(f"Pada suhu {temp}°C, air akan mencair.")

else:
    print(f"Pada suhu {temp}°C, air akan menguap.")