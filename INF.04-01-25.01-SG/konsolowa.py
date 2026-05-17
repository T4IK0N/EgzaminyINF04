import random

class Klasa:
    def __init__(self, rozmiar_tablicy):
        self.__tablica_liczb = []
        self.__liczba_elementow = rozmiar_tablicy

        for i in range(self.__liczba_elementow):
            self.__tablica_liczb.append(random.randint(1, 1000))

    def wyswietl_tablice(self):
        print("Wszystkie elementy tablicy: ")
        for index, element in enumerate(self.__tablica_liczb):
            print(f"{index}: {element}")

    def szukaj(self, szukana):
        for index, element in enumerate(self.__tablica_liczb):
            if element == szukana:
                return index
        return -1

    def nieparzyste(self):
        print("Liczby nieparzyste: ")
        count = 0
        for index, element in enumerate(self.__tablica_liczb):
            if element % 2 != 0:
                count += 1
                print(element)
        return count

    def srednia(self):
        suma = 0
        for element in self.__tablica_liczb:
            suma += int(element)
        return suma / self.__liczba_elementow


klasa = Klasa(30)
klasa.wyswietl_tablice()

szukana_wynik = klasa.szukaj(52)
if szukana_wynik != -1:
    print("Znaleziono liczbę, indeks w tablicy: ", szukana_wynik)

print("Nieparzyste liczba: ", klasa.nieparzyste())

print("Średnia elementów tablicy: ", klasa.srednia())