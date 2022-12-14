print("Program Huruf Vokal dan Konsonan\n")

vokal = ['A','I','U','E','O']

huruf = input("Masukkan sebuah huruf: ")

if huruf.upper() in vokal:
    print(f"\n{huruf} adalah salah satu huruf vokal.")