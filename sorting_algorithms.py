import random, math
from values import width, height

# bubble_sort(arr)
def bubble_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(len(temp)):
        for j in range(len(temp) - i - 1):
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
            yield temp, j + 1

# selection_sort(arr)
def selection_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(len(temp)):
        min_index = i

        for j in range(i + 1, len(temp)):
            if temp[j] < temp[min_index]:
                min_index = j

        temp[i], temp[min_index] = temp[min_index], temp[i];
        yield temp, min_index

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
        yield temp, prev_indx + 1

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return list(merge(left,right))


def merge(left, right):
    res = []

    while len(left) and len(right):
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    if len(left):
        res += left
    else:
        res += right

    return res


def generate_data(size : int) -> list[float]:
    for i in range(size):
        #it should go from 0 to height
        return shuffle_data([i * height / size for i in range(size)])
    #return [random.randint(10, height - 10) for _ in range(size)]


def shuffle_data(arr : list[float]) -> list[float]:
    random.shuffle(arr)
    return arr
