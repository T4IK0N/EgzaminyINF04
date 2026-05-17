from abc import ABC, abstractmethod

class Pytanie(ABC):
    def __init__(self, tresc_pytania, nazwa_pliku):
        self._tresc_pytania = tresc_pytania
        self._nazwa_pliku = nazwa_pliku
        self._poprawna = False

    @abstractmethod
    def sprawdz_odpowiedz(self, odpowiedz: str) -> bool:
        pass

class PytanieZamkniete(Pytanie):
    def __init__(self, tresc_pytania, nazwa_pliku, odpowiedz_a, odpowiedz_b, odpowiedz_c,
                 odpowiedz_poprawna):
        super().__init__(tresc_pytania, nazwa_pliku)
        self.__odpowiedz_a = odpowiedz_a
        self.__odpowiedz_b = odpowiedz_b
        self.__odpowiedz_c = odpowiedz_c
        self.__odpowiedz_poprawna = odpowiedz_poprawna

    def sprawdz_odpowiedz(self, odpowiedz: str) -> bool:
        if odpowiedz == self.__odpowiedz_poprawna:
            self._poprawna = True
        else:
            self._poprawna = False
        return self._poprawna