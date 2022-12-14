def binarySearch(nim, keyword):
    print(f"Data: {nim}")

    low = 0
    high = len(nim) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if nim[mid] == keyword:
            print(f"NIM {keyword} ditemukan pada index ke-{mid}")
            return mid
        elif str(nim[mid]) < str(keyword):
            low = mid + 1
        else:
            high = mid - 1

    print(f"Error! NIM {keyword} tidak ditemukan!")
    return -1

nim = [12102002, 121002004, 12102001, 12102003, 12102005, 12102008, 12102007, 12102006, 12102009, 121020013, 12102010, 12102012, 12102011]
keyword = int(input("Masukkan NIM: "))

binarySearch(nim, keyword)