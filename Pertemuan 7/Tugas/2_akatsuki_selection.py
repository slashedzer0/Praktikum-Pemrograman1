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

akatsuki = ['Pain', 'Konan', 'Tobi', 'Zetsu', 'Sasori', 'Hidan', 'Deidara', 'Kisame', 'Kakuzu', 'Itachi']

# pembuktian
print(f"Before  : {akatsuki}")
selection_sort(akatsuki)
print(f"After   : {akatsuki}")