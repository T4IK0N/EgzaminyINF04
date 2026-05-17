
class Urzadzenie:
    """
    ************
    nazwa: wyswietl_komunikat
    opis: wyświetla (przy pomocy print) komunikat podany w argumencie
    parametry: komunikat - komunikat który chcemy zwrócić
    zwracany typ i opis: brak
    autor: numer_zdajacego
    ************
    """
    def wyswietl_komunikat(self, komunikat):
        print(komunikat)

class Pralka(Urzadzenie):
    def __init__(self):
        self.__numer_prania = 0

    def ustaw_numer_prania(self, numer_programu):
        if numer_programu in range(1, 13):
            self.__numer_prania = numer_programu
        else:
            self.__numer_prania = 0
        return self.__numer_prania

class Odkurzacz(Urzadzenie):
    def __init__(self):
        self.__stan_odkurzacza = False

    def on(self):
        if not self.__stan_odkurzacza:
            self.__stan_odkurzacza = True
            self.wyswietl_komunikat("Odkurzacz włączono")

    def off(self):
        if self.__stan_odkurzacza:
            self.__stan_odkurzacza = False
            self.wyswietl_komunikat("Odkurzacz wyłączono")

if __name__ == "__main__":
    pralka = Pralka()
    odkurzacz = Odkurzacz()
    numer_input = int(input("Podaj numer prania 1..12"))
    if pralka.ustaw_numer_prania(numer_input) != 0:
        print("Program został ustawiony")
    else:
        print("Podano niepoprawny numer programu")

    odkurzacz.on()
    odkurzacz.on()
    odkurzacz.on()
    odkurzacz.wyswietl_komunikat("Odkurzacz wyładował się")
    odkurzacz.off()