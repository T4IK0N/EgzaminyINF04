import random

class Main:
    def __init__(self):
        self.tablica = []

    def wypelnij_tablice(self):
        for i in range(50):
            self.tablica.append(random.randint(1, 100))

    def przeszukaj_tablice(self, szukana_wartosc):
        self.tablica.append(szukana_wartosc)
        for index, value in enumerate(self.tablica):
            if value == szukana_wartosc and index != len(self.tablica)-1:
                print(", ".join(str(element) for element in self.tablica))
                print(f"Wartość {szukana_wartosc} znaleziona na pozycji: {index}")
                return
            elif value == szukana_wartosc and index == len(self.tablica)-1:
                print(", ".join(str(element) for element in self.tablica))
                print(f"Wartość {szukana_wartosc} nie została znaleziona w tablicy.")
                return

main = Main()
main.wypelnij_tablice()
main.przeszukaj_tablice(int(input("Podaj szukaną wartość: ")))