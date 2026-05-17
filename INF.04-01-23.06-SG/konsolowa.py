"""Ze zbioru liczb naturalnych z przedziału [2, n], tj. {2,3,4,... ,n} wybieramy najmniejszą, czyli 2, i wykreślamy
wszystkie jej wielokrotności większe od niej samej, to jest 4, 6, 8, ... . Z pozostałych liczb wybieramy
najmniejszą niewykreśloną liczbę (3) i wykreślamy wszystkie jej wielokrotności większe od niej samej: 6,
9, 12, ... . Według tej samej procedury postępujemy dla liczby 5. Następnie dla 7 aż do sprawdzenia
wszystkich niewykreślonych wcześniej liczb. Wykreślanie powtarzamy do momentu, gdy liczba i, której
wielokrotność wykreślamy, będzie większa niż √𝑛."""
import math

n = 100
A = []
def wypelnij_tablice(A: list):
    for i in range(n):
        A.append(True)
    A[0], A[1] = False, False

def is_prime():
    wypelnij_tablice(A)
    for i in range(2, int(math.sqrt(n))):
        if A[i]:
            for j in range(i*i, n, i):
                #zacznij od kwadratu liczby i / skoncz przy n / skacz co i (np 2 4 6 8)
                A[j] = False

    wynik = ""
    for i, j in enumerate(A):
        if j:
            wynik += f"{i}, "
    return wynik

print(is_prime())