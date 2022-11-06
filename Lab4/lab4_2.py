import random

x = int(input("Podaj liczbe elementów: "))
lista1 = []
for i in range (x):
    n = random.randint(1,10)
    lista1.append(n)
print(lista1)

x1 = int(input("Podaj liczbe elementów dla drugiej listy: "))
lista2 = []
for i in range (x1):
    n2 = random.randint(5,15)
    lista2.append(n2)
print(lista2)

x2 = int(input("Podaj liczbe której szukasz: "))
if x2 in lista1:
    print("Liczba występuje w lista1")
elif x2 in lista2:
    print("Liczba występuje w lista2")
else:
    print("Liczba występuje w obu zestawach")

print("DODATEK")

lista_1_2 = lista1 + lista2

lista_1_2.sort()

print(lista_1_2)