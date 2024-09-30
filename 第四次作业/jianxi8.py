def parent(num):
    return num/2

def left(num):
    return num*2

def right(num):
    return num*2+1

def heapify(arr, n, i):
    biggest=i

    if left(i) < n and arr[left(i)] > arr[biggest]:
        biggest = left(i)

    if right(i) < n and arr[right(i)] > arr[biggest]:
        biggest = right(i)

    if biggest != i:
        arr[i], arr[biggest] = arr[biggest], arr[i]
        heapify(arr, n, biggest)

def build_min_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def tree_sort(arr):
    build_min_heap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


arr = [8, 3, 10, 1, 6, 14, 4, 7, 13]
sorted_arr = tree_sort(arr)
print(sorted_arr)
