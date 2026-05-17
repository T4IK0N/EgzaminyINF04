import unittest
from konsolowa import szyfrowanie


class TestSzyfrowanie(unittest.TestCase):

    def test_dane_podstawowe(self):
        self.assertEqual(szyfrowanie("abc", 3), "def")

    def test_zawijanie_alfabetu(self):
        self.assertEqual(szyfrowanie("xyz", 3), "abc")

    def test_odszyfrowanie_klucz_ujemny(self):
        self.assertEqual(szyfrowanie("def", -3), "abc")

    def test_klucz_wiekszy_niz_alfabet(self):
        self.assertEqual(szyfrowanie("abc", 29), "def")

    def test_spacja_w_tekscie(self):
        self.assertEqual(szyfrowanie("ab cd", 2), "cd ef")


if __name__ == "__main__":
    unittest.main()
