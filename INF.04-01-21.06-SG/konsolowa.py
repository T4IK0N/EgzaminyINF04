class Klasa:
    def __init__(self):
        self.tablica = [0] * 10

    def wprowadz_tablice(self):
        for index, value in enumerate(self.tablica):
            self.tablica[index] = int(input(f"Wprowadź liczbę {index+1}: "))

    def sortowanie(self):
        for i in range(len(self.tablica)):
            for j in range(len(self.tablica)):
                if self.tablica[i] > self.tablica[j]:
                    temp = self.tablica[j]
                    self.tablica[j] = int(self.tablica[i])
                    self.tablica[i] = temp
        return self.tablica

    def wartosc_najwieksza(self):
        wartosc_najwieksza = 0
        for i in range(len(self.tablica)):
            if int(self.tablica[i]) > wartosc_najwieksza:
                wartosc_najwieksza = int(self.tablica[i])
        return wartosc_najwieksza

klasa = Klasa()
klasa.wprowadz_tablice()
print(klasa.wartosc_najwieksza())
print(klasa.sortowanie())