import random

# bubble_sort(arr)
def bubble_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(len(temp)):
        for j in range(len(temp) - i - 1):
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
            yield temp

# selection_sort(arr)
def selection_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(len(temp)):
        min_index = i

        for j in range(i + 1, len(temp)):
            if temp[j] < temp[min_index]:
                min_index = j

        temp[i], temp[min_index] = temp[min_index], temp[i];
        yield temp

# insertion_sort(arr)
def insertion_sort(arr : list[float]) -> list[float]:
    for i in range(1, len(arr)):
        key = arr[i]
        prev_indx = i - 1
        while prev_indx >= 0 and key < arr[prev_indx]:
            arr[prev_indx + 1] = arr[prev_indx]
            prev_indx -= 1
        arr[prev_indx + 1] = key
        yield arr
