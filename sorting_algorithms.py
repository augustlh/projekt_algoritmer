import random, math
from values import width, height

# bubble_sort(arr)
def bubble_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(len(temp)):
        for j in range(len(temp) - i - 1):
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
            yield temp, j + 1, j

# selection_sort(arr)
def selection_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(len(temp)):
        min_index = i

        for j in range(i + 1, len(temp)):
            if temp[j] < temp[min_index]:
                min_index = j

        temp[i], temp[min_index] = temp[min_index], temp[i];
        yield temp, min_index, i

# insertion_sort(arr)
def insertion_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(1, len(temp)):
        key = temp[i]
        prev_indx = i - 1
        while prev_indx >= 0 and key < temp[prev_indx]:
            temp[prev_indx + 1] = temp[prev_indx]
            prev_indx -= 1
        temp[prev_indx + 1] = key
        yield temp, prev_indx + 1, i

def quick_sort(arr : list[float]) -> list[float]:
    pass


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

        yield arr, k, -1
                

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        yield arr, 0, -1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
                
        yield arr, 0, -1

def mergeSort(arr, l= 0, r=None):
    if r is None:
        r = len(arr) - 1

    if l < r:
        m = (l + r) // 2

        yield from mergeSort(arr, l, m)
        yield from mergeSort(arr, m + 1, r)
        yield from merge(arr, l, m, r) 

def augussySort(arr, l= 0, r= 1):
    n = len(arr)
    current_size = 1

    while current_size < n:
        left = 0

        while left < n - 1:
            mid = min((left + current_size - 1), (n - 1))
            right = ((2 * current_size + left - 1, n - 1)[2 * current_size + left - 1 > n - 1])
            yield from merge(arr, left, mid, right)
            left = left + current_size * 2

        current_size = 2 * current_size


def generate_data(size : int, type : str) -> list[float]:
    if type == "bar":
        for i in range(size):
            return shuffle_data([i * height / size for i in range(size)])
    else:
        for i in range(size):
            return shuffle_data([i for i in range (size)])


def shuffle_data(arr : list[float]) -> list[float]:
    random.shuffle(arr)
    return arr
