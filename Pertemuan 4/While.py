login_chance = 3

while login_chance > 0:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    login_success = (username == "admin") and (password == "admin")

    if login_success:
        print("Login berhasil!")
        break

    else:
        login_chance = login_chance - 1
        print(f"Login gagal! Kesempatan mencoba: {login_chance}")