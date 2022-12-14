# 2 style penulisan fungsi:
# linearSearch()
# linear_search()

#---------------------------------------------------------------
### LINEAR SEARCH
def linearSearch(data, keyword):
    print(f"Data: {data}")

    for i in range(len(data)):

        if str(data[i]).lower() == keyword.lower():
            print(f"{keyword} ditemukan pada index ke-{i}")
            return i

    print(f"Error! {keyword} tidak ditemukan!")
    return -1


### INSERTION SORT (ascending)
def insertionSort(data):
    for i in range(1, len(data)):
        item = data[i]
        j = i - 1

        while j >= 0 and data[j] > item:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = item

    return data


### DATA STRING CONVERSION
def dataConversion(data):
    convertedData = []

    for i in data:
        convertedData.append(str(i).lower())
    return convertedData


### BINARY SEARCH
def binarySearch(data, keyword): 
    convertedData = dataConversion(data)
    sortedData = insertionSort(convertedData)
    
    print(f"Data (diurutkan): {sortedData}")
    
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if sortedData[mid] == keyword:
            print(f"{keyword} ditemukan pada index ke-{mid}")
            return mid
        elif str(sortedData[mid]) < str(keyword):
            low = mid + 1
        else:
            high = mid - 1

    print(f"Error! {keyword} tidak ditemukan!")
    return -1


### MAIN (linear / binary search)
data = [7, 4, 2, 'N', 'L', 6, 0, 9, 'F']
keyword = input("Masukkan kata kunci: ")

# uncomment salah satu!
#linearSearch(data, keyword)
binarySearch(data, keyword)