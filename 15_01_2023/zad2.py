
#zadanie 2

def oblicz(liczba1, liczba2):
    print("Liczba pierwsza: ",liczba1, "Liczba druga: ",liczba2)

    return liczba1+liczba2, liczba1-liczba2
print(oblicz(1,2))

krotka=oblicz(2,4)
print(krotka[0], krotka[1])
l1, l2=oblicz(3.5, 0.6)
print(l1, l2)