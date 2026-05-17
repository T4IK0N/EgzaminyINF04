import random

class Main:
    def __init__(self, n):
        self.n = n
        self.tab = []
        self.lista = []

    def wypelnij_tablice(self):
        for i in range(self.n):
            temp = []
            for j in range(6):
                temp.append(random.randint(1, 49))
            self.tab.append(temp)

        for i in range(self.n):
            for j in range(6):
                self.lista.append(self.tab[i][j])

    def wyswietl(self):
        print("Zestawy wylosowanych losowań:")
        for i in range(self.n):
            print(f"Losowanie {i+1}: {self.tab[i]}")
        for i in range(1, 50):
            ilosc = 0
            for j in self.lista:
                if i == j:
                    ilosc+=1
            print(f"Wystąpienia liczby {i}: {ilosc}")

main = Main(int(input("Ile wygenerować losowań?\n")))
main.wypelnij_tablice()
main.wyswietl()