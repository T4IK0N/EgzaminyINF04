import math

n = 100
A = []
"""
***
nazwa funkcji: wypelnij_tablice
parametry wejściowe: A - przechowuje liste
wartość zwracana: brak
informacje: funkcja wypełnia tablice A (podaną jako argument) wartościami True (oprócz dla 1 i 2 indeksu - tam ustawia False)
autor: numer_zdajacego
***
"""
def wypelnij_tablice(A: list):
    for i in range(n):
        A.append(True)
    A[0], A[1] = False, False

def is_prime():
    wypelnij_tablice(A)
    for i in range(2, int(math.sqrt(n))):
        if A[i]:
            for j in range(i*i, n, i):
                A[j] = False

    wynik = ""
    for i, j in enumerate(A):
        if j:
            wynik += f"{i}, "
    return wynik

print("Liczby pierwsze: "+is_prime())