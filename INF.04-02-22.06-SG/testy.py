from konsolowa import Osoba

print(f"Liczba zarejestrowanych osób to {Osoba.liczba_instancji}")

id = int(input("Podaj id osoby: "))
imie = input("Podaj imię osoby: ")

osoba1 = Osoba()
osoba2 = Osoba(id=id, imie=imie)
osoba3 = Osoba.metoda_kopiujaca(osoba2)

osoba1.wypisz_imie("Jan")
osoba2.wypisz_imie("Jan")
osoba3.wypisz_imie("Jan")

print(f"Liczba zarejestrowanych osób to {Osoba.liczba_instancji}")