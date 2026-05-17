def sprawdz_plec(pesel: str):
    if int(pesel[9]) % 2 == 0:
        return 'K'
    else:
        return 'M'

"""
**********************************************
nazwa funkcji: sprawdz_zgodnosc
opis funkcji: sprawdza zgodnosc argumentu "pesel" na podstawie sumy kontrolnej
parametry: pesel - argument typu łańcucha znaków, reprezentuje numer pesel
zwracany typ i opis: bool - zwraca True jeśli pesel się zgadza albo False jeśli się nie zgadza
autor: numer_zdajacego
***********************************************
"""
def sprawdz_zgodnosc(pesel: str) -> bool:
    ostatnia = int(pesel[-1])
    pesel = pesel[:-1]
    waga = "1379137913"
    S = 0

    for index, value in enumerate(pesel):
        S += int(value) * int(waga[index])

    M = int(S % 10)
    if M == 0:
        R = 0
    else:
        R = 10-M

    if R == ostatnia:
        return True
    else:
        return False

pesel_input = input("Wprowadź numer pesel: ")
plec = sprawdz_plec(pesel_input)
if plec == 'K':
    print("Płeć osoby: Kobieta")
else:
    print("Płeć osoby: Mężczyzna")

czy_sie_zgadza = sprawdz_zgodnosc(pesel_input)
if czy_sie_zgadza:
    print("Czy pesel się zgadza: Tak")
else:
    print("Czy pesel się zgadza: Nie")