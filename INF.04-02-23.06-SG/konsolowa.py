def sortowanie(tablica):
    for i in range(len(tablica)):
        for j in range(len(tablica)-1):
            if tablica[j] > tablica[j+1]:
                tablica[j], tablica[j+1] = tablica[j+1], tablica[j]

    for i in range(len(tablica)):
        print(tablica[i])

sortowanie([5, 1, 25, 1236, 2, 60])