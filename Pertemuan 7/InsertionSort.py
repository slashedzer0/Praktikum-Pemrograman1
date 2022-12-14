import timeit

def insertion_sort(array):
    start = timeit.default_timer()
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1
        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item
    stop = timeit.default_timer()

    print(f"Insertion Sort successful! Elapsed time: {stop - start}")
    return array

list_i = [4, 1, 2, 5, 3, 7, 8]

# pembuktian
print(f"Before  : {list_i}")
insertion_sort(list_i)
print(f"After   : {list_i}")