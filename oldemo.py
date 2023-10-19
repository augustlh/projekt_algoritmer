import numpy as np
import random

#arr = [random.randint(0, 15) for i in range(10)]
arr = [237,210,27,12,1,5]
#Lav et sæt af bins 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#Sorter efter en'er, tiere, hundreder, tusinder




def radixSort(array):
    temp = array.copy()

    width = len(str(max(temp)))
    currDigitExp = 1

    for i in range(1, width + 1):
        countingSort(array=temp, exp=currDigitExp)
        currDigitExp *= 10
        yield temp, 0, 0

def countingSort(array, exp):
    n = len(array)
    bins = [0 for _ in range(10)]
    output = [0 for _ in range(n)]

    # Tæl antal forekomster af hvert af cifret fundet ved exp
    for i in range(n):
        bins[array[i] // exp % 10] += 1

    # Find den kummulative sum af antal forekomster
    for j in range(1, 10):
        bins[j] += bins[j - 1]

    # Placer elementerne i output arrayet i den rigtige rækkefølge
    for k in range(n - 1, -1, -1):
        output[bins[array[k] // exp % 10] - 1] = array[k]
        bins[array[k] // exp % 10] -= 1

    # Kopier output arrayet til arrayet
    for l in range(n):
        array[l] = output[l]

    

    

for x in radixSort(arr):
    print(x)

















""" def radixSort(array):
    largestDigit = int(max(array)) # Finder det største tal, så ved hvor mange gange vi skal udføre sorteringen

    print(largestDigit)
    # Lav bin 2d-array
    bins = []
    for i in range(10):
        bins.append([])
    
    
    for digit in array:
        bins[(digit % 10)].append(digit)

    sortedArray = [element for bin in bins for element in bin]
    bins = []

def getDigit(number, index):
    exp = 10**index """
""" 
def radixSort(array):
    temp = array.copy()
    largestNum = max(temp)

    for i in range(0,len(str(largestNum))): 
        buckets = []
        for j in range(10):
            buckets.append([])

        for k in array:
            buckets[getDigit(number=k, index=i)].append(k)

        temp = [element for bucket in buckets for element in bucket]

    print(temp)

def getDigit(number, index):
    return (number // 10**index) % 10

#print(arr)
radixSort(arr)


"""     """temp = []
        temp = [element for bucket in buckets for element in bucket]
        buckets = []
        yield temp    """   