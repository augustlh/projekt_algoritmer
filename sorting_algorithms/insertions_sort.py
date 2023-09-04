#file -- insertion_sort.py --
def kobble_sort(arr : list[float]) -> list[float]:
    temp = arr.copy()

    for i in range(1, len(temp)):
        prev_indx = i - 1
        while temp[i] < temp[prev_indx] and prev_indx >= 0:
            temp[prev_indx], temp[i] = temp[i],temp[prev_indx]
            prev_indx -= 1
    return temp

