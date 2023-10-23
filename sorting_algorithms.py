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

def stalin_sort(arr : list[float]):
    i = 0
    while i < len(arr) - 1:
        if arr[i] > arr[i + 1]:
            arr.pop(i + 1) 
        else: i += 1
        yield arr, i+1,i

def radix_sort(array : list[int]):
    temp = array.copy()

    for i in range(len(temp)):
        temp[i] = int(temp[i])


    width = len(str(max(temp)))
    currDigitExp = 1

    for i in range(1, width + 1):
        yield from counting_sort(array=temp, exp=currDigitExp)
        currDigitExp *= 10

    

def counting_sort(array : list[int], exp : int):
    k = len(array)
    bins = [0 for _ in range(10)]
    output = array.copy()

    # Tæl antal forekomster af hvert af cifret fundet ved exp
    for i in range(k):
        bins[array[i] // exp % 10] += 1
        yield output, i, -1

    # Find den kummulative sum af antal forekomster
    for j in range(1, 10):
        bins[j] += bins[j - 1]

    # Placer elementerne i output arrayet i den rigtige rækkefølge
    for p in range(k - 1, -1, -1):
        output[bins[array[p] // exp % 10] - 1] = array[p]
        bins[array[p] // exp % 10] -= 1
        
        yield output, bins[array[p] // exp % 10] - 1, p # ændre til -1, hvis ikke du vil have den grønne bar



    # Kopier output arrayet til arrayet
    for l in range(k):
        array[l] = output[l]
    #    #yield array, l, bins[]


# Inspireret af https://www.geeksforgeeks.org/python-program-for-merge-sort/
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = arr[l:m+1]
    R = arr[m+1:r+1]

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
