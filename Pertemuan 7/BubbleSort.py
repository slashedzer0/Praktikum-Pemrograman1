import timeit

def bubble_sort(array):
    start = timeit.default_timer()
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    stop = timeit.default_timer()

    print(f"Bubble Sort successful! Elapsed time: {stop - start}")
    return array

list_b = [7, 5, 4, 3, 9, 11]

# pembuktian
print(f"Before  : {list_b}")
bubble_sort(list_b)
print(f"After   : {list_b}")