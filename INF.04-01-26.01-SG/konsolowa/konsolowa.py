import random

class Kosc:
    liczba_instancji = 0
    def __init__(self, wartosc=None):
        self.nazwy_plikow = ["kosc0.png", "kosc1.png", "kosc2.png", "kosc3.png", "kosc4.png", "kosc5.png", "kosc6.png"]
        self.liczba_oczek: int = 0
        self.identyfikator_pliku: int = 0
        self.czy_kosc_dostepna: bool = True
        if wartosc is None:
            wartosc = random.randint(1, 6)
            self.liczba_oczek = wartosc
            self.identyfikator_pliku = wartosc
            self.czy_kosc_dostepna = True
        else:
            wartosc = int(wartosc)
            if wartosc not in [1, 2, 3, 4, 5, 6]:
                wartosc = 0
            self.liczba_oczek = wartosc
            self.identyfikator_pliku = wartosc
            self.czy_kosc_dostepna = True

        Kosc.liczba_instancji += 1

    def rzut_koscia(self):
        if self.czy_kosc_dostepna:
            wartosc = random.randint(1, 6)
            self.liczba_oczek = wartosc
            self.identyfikator_pliku = wartosc
    def blokuj_kosc(self):
        self.czy_kosc_dostepna = False
    def zwroc_wartosc(self) -> str:
        dictoniary = {
            0: "zero",
            1: "jeden",
            2: "dwa",
            3: "trzy",
            4: "cztery",
            5: "pięć",
            6: "sześć"
        }
        return dictoniary[self.identyfikator_pliku]

if __name__ == "__main__":
    kosc1 = Kosc()
    print("Liczba instancji 1:", Kosc.liczba_instancji)
    print("Kość 1 liczba oczek liczbowo:", kosc1.liczba_oczek)
    print("Kość 1 liczba oczek tekstowo:", kosc1.zwroc_wartosc())
    print("Kość 1 nazwa pliku: ", kosc1.nazwy_plikow[kosc1.identyfikator_pliku])
    kosc2 = Kosc(int(input("Wprowadź wartość: ")))
    print("Liczba instancji 2:", Kosc.liczba_instancji)
    print("Kość 2 liczba oczek liczbowo:", kosc2.liczba_oczek)
    print("Kość 2 liczba oczek tekstowo:", kosc2.zwroc_wartosc())
    print("Kość 2 nazwa pliku: ", kosc2.nazwy_plikow[kosc2.identyfikator_pliku])
