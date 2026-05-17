class Film:
    def __init__(self):
        self._tytul = ""
        self._liczba_wypozyczen = 0

    def set_tytul(self, tytul):
        self._tytul = tytul
    def get_tytul(self):
        return self._tytul
    def get_liczbe_wypozyczen(self):
        return self._liczba_wypozyczen
    def inkremetuj_liczbe_wypozyczen(self):
        self._liczba_wypozyczen+=1

if __name__ == "__main__":
    film = Film()
    film.set_tytul("Pianista")
    print(film.get_tytul())
    print("Liczba wypozyczen przed:", film.get_liczbe_wypozyczen())
    film.inkremetuj_liczbe_wypozyczen()
    print("Liczba wypozyczen po:", film.get_liczbe_wypozyczen())