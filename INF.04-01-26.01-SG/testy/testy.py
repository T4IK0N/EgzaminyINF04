import unittest
from konsolowa.konsolowa import Kosc

class Test(unittest.TestCase):
    def test_greater_than_6(self):
        kosc = Kosc(2)
        kosc.rzut_koscia()
        #jesli bedzie niżej będzie błąd jeśli będzie wyżej, przejdzie test
        self.assertLessEqual(kosc.liczba_oczek, 6)
    def test_less_than_1(self):
        kosc = Kosc(2)
        kosc.rzut_koscia()
        #jesli bedzie wyzej będzie błąd jeśli będzie niżej, przejdzie test
        self.assertGreaterEqual(kosc.liczba_oczek, 1)
    def test_kosc_niedostepna(self):
        kosc = Kosc(2)
        kosc_wartosc_poczatkowa = kosc.liczba_oczek
        kosc.blokuj_kosc()
        kosc_wartosc_koncowa = kosc.liczba_oczek
        self.assertEqual(kosc_wartosc_poczatkowa, kosc_wartosc_koncowa)

if __name__ == "__main__":
    unittest.main()