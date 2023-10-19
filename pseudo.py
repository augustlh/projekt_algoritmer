def radixSort(array):
    # Find den maksimale værdi i arrayet og bestem bredden (antallet af cifre) af det
    A = width(max(array))
    
    # Bestem det nuværende cifre, som vi sorterer efter (1'er, 10'ere, 100'ere, etc.) 
    exp = 1

    # For hvert cifre i bredden, sorter arrayet ved hjælp af counting sort
    for i in range(1, A + 1):
        array = countingSort(array, exp)

        # Gå videre til næste cifre
        exp *= 10
    
    
def countingSort(A, digit):

    # A og B er input og output lister med længde n
    # count er en liste med længde 10, hvis værdier er forekomster af et givent cifre (starter alle med at være 0)

    # Find antallet af forekomster af hvert cifre i A på digit pladsen
    loop fra j = 0 til len(A):
        # Find det cifre, som vi sorterer efter. Findes ved at dividere med vores nuværende tal med 10^(digit) og derefter tage modulo 10
        # F.eks. 237 // 1^2 % 10 = 7 eller 237 // 10^2 % 10 = 2
        count[A[j] // digit % 10] += 1
    
    # Find den kummulative sum af antal forekomster
    loop fra i = 1 til 10:
        count[i] += count[i - 1]
    
    # Placer elementerne i output arrayet i den rigtige rækkefølge
    loop fra j = n - 1 til 0:
        B[count[A[j] // digit % 10] - 1] = A[j]
        count[A[j] // digit % 10] -= 1
    
    return B