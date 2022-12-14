import timeit

def selection_sort(array):
    start = timeit.default_timer()
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    stop = timeit.default_timer()

    print(f"Selection Sort successful! Elapsed time: {stop - start}")
    return array

list_x = [6, 8, 0, 10, 2, 4]

# pembuktian
print(f"Before  : {list_x}")
selection_sort(list_x)
print(f"After   : {list_x}")