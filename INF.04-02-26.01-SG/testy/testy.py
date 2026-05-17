from konsolowa.konsolowa import Pytanie, PytanieZamkniete

# pytanie = Pytanie("tresc_pytania", "nazwa_pliku")

pytanieZamkniete = PytanieZamkniete(
    input("Treść pytania: "),
    input("Nazwa pliku: "),
    input("Odpowiedź A: "),
    input("Odpowiedź B: "),
    input("Odpowiedź C: "),
    input("Odpowiedź Poprawna: ")
)

odpowiedzNaPytanie = input("Odpowiedź na pytanie")

if pytanieZamkniete.sprawdz_odpowiedz(odpowiedzNaPytanie):
    print("Odpowiedź prawidłowa")
else:
    print("Odpowiedź nieprawidłowa")