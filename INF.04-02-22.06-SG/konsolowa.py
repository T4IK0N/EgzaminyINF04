class Osoba:
    liczba_instancji = 0

    def __init__(self, id=0, imie=""):
        self.__id = id
        self.__imie = imie
        Osoba.liczba_instancji += 1

    @classmethod
    def metoda_kopiujaca(cls, osoba):
        return cls(osoba.__id, osoba.__imie)

    def wypisz_imie(self, imie):
        if self.__imie:
            print(f"Cześć {imie}, mam na imię {self.__imie}")
        else:
            print("Brak danych")