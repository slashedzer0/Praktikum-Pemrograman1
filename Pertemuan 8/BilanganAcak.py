aux_arr = []

def make_aux_array(arr, n):
	global aux_arr

	for i in range(n):
		aux_arr.append([arr[i], i])
		
	aux_arr.sort()

def binarySearch(arr, n, x):
	global aux_arr
	
	position = n
	for i in range(n):
		if aux_arr[i][0] == x:
			position = i
			
			return aux_arr[position][1]
	return -1

def printFunc(arr, n, x):
	global aux_arr
	make_aux_array(arr, n)
	result = binarySearch(arr, n, x)

	if result == -1:
		print((f"Error! {x} tidak ditemukan!"))
	else:
		print(f"{x} ditemukan pada index ke-{result}")

arr = [21, 61, 28, 72, 44, 68, 37, 52, 75, 71]
N = len(arr)
X = int(input("Masukkan bilangan: "))

printFunc(arr, N, X)