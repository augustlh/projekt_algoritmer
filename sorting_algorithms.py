# August Leander Hedman
# augu1789@edu.nextkbh.dk
# NEXT Sukkertoppen, S3n    

# Model delen af MVC.

# Importer relevante biblioteker og funktioner osv. fra andre filer i programmet
import random, math
from values import width, height
from typing import Iterator, Union, Tuple, List

# Bemærk, at alle funktionerne nedenfor er mere eller mindre skabt ud fra pseudokode fra "https://codecrucks.com/sorting-algorithm/"

# En generator funktion, som udfører bubble_sort på et givent array. 
# Denne funktion tager en liste som input og returnerer en iterator, der genererer
# en tuple efter hvert trin i sorteringen. Tuplen indeholder den midlertidige liste og
# indeksert for de to elementer, der blev sammenlignet i trinnet.
def bubble_sort(arr: List[float]) -> Iterator[Tuple[List[float], int, int]]:
    # Laver et temp array, så der ikke er side effects
    temp = arr.copy()
    
    # Gennemgår alle elementer i arrayet
    for i in range(len(temp)):
        for j in range(len(temp) - i - 1):
            # Hvis det næste tal er mindre end det nuværende, så byt plads
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
            yield temp, j + 1, j

# selection_sort(arr)
def selection_sort(arr: List[float]) -> Iterator[Tuple[List[float], int, int]]:
    temp = arr.copy()

    # Iterererer over alle elementer i arrayet
    for i in range(len(temp)):
        # Tildeler min_index værdien i, som start
        min_index = i

        # Itererer over alle elementer efter i
        for j in range(i + 1, len(temp)):
            # Hvis det næste tal er mindre end det nuværende, så sæt min_index til j
            if temp[j] < temp[min_index]:
                min_index = j
        # Bytter plads på det nuværende element og det mindste element
        temp[i], temp[min_index] = temp[min_index], temp[i];
        yield temp, min_index, i

# insertion_sort(arr)
def insertion_sort(arr: List[float]) -> Iterator[Tuple[List[float], int, int]]:
    temp = arr.copy()

    for i in range(1, len(temp)):
        key = temp[i]
        prev_indx = i - 1
        while prev_indx >= 0 and key < temp[prev_indx]:
            temp[prev_indx + 1] = temp[prev_indx]
            prev_indx -= 1
        temp[prev_indx + 1] = key
        yield temp, prev_indx + 1, i

# stalin_sort(arr)
def stalin_sort(arr: List[float]) -> Iterator[Tuple[List[float], int, int]]:
    i = 0
    while i < len(arr) - 1:
        # Hvis det næste tal er mindre end det nuværende, så fjern det
        if arr[i] > arr[i + 1]:
            arr.pop(i + 1) 
        else: i += 1
        yield arr, i+1,i

# radix_sort(arr)
def radix_sort(array : list[int]) -> Iterator[Tuple[List[int], int, int]]:
    temp = array.copy()
    
    # Parse alle tal i arrayet som integers
    for i in range(len(temp)):
        temp[i] = int(temp[i])

    # Find bredden af det største tal i arrayet
    width = len(str(max(temp)))

    # Hvilket ciffer skal vi sortere efter?
    currDigitExp = 1

    # Sorter efter alle cifre
    for i in range(1, width + 1):
        # Sorter efter det nuværende ciffer
        yield from counting_sort(array=temp, exp=currDigitExp)
        # Gå videre til det næste ciffer
        currDigitExp *= 10

# counting_sort(array, exp)
def counting_sort(array : List[int], exp : int) -> Iterator[Tuple[List[int], int, int]]:
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


def merge_sort(arr: List[Union[int, float]], l: int = 0, r=None) -> Iterator[Tuple[List[Union[int, float]], int, int]]:
    if r is None:
        r = len(arr) - 1

    if l < r:
        # Find midten af arrayet
        m = (l + r) // 2

        # Kald merge_sort rekursivt på venstre og højre side af arrayet
        yield from merge_sort(arr, l, m)
        yield from merge_sort(arr, m + 1, r)

        yield from combine(arr, l, m, r) 

def combine(arr: List[Union[int, float]], l: int, m: int , r: int) -> Iterator[Tuple[List[Union[int, float]], int, int]]:
    # Beregn længden af de to del-lister
    l1 = m - l + 1
    l2 = r - m

    # Midlertidige arrays 
    left = [0] * (l1 + 1)
    right = [0] * (l2 + 1)

    # Kopier data til de midlertidige arrays
    for i in range(l1):
        left[i] = arr[l + i]

    for j in range(l2):
        right[j] = arr[m + j + 1]

    left[l1] = math.inf
    right[l2] = math.inf

    i = 0
    j = 0

    # Sammenlign elementerne i de to del-lister og kombiner dem i  arr
    for k in range(l, r + 1):
        if left [i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        yield arr, k, -1

def generate_data(size : int, type : str) -> list[float]:
    if type == "bar":
        return shuffle_data([i * height / size for i in range(size)])
    else:
        return shuffle_data([i for i in range(size)])


def shuffle_data(arr : List[float]) -> List[float]:
    random.shuffle(arr)
    return arr
