import timeit

# algoritma bubble sort dari terbesar ke terkecil
def bubble_sort(array):
    start = timeit.default_timer()
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    stop = timeit.default_timer()

    print(f"Bubble Sort successful! Elapsed time: {stop - start}")
    return array

ips = [3.8, 2.9, 3.3, 4.0, 2.4]

# pembuktian
print(f"Before  : {ips}")
bubble_sort(ips)
print(f"After   : {ips}")