
def potega(L1, L2):
    L3 = []
    if len(L1)!=len(L2):
        return None
    for i in range(len(L1)):
        L3.append(L1[i]**L2[i])

    return L3

wynik = potega([4, 3, 5, 6], [2, 7, 3, 4])

print(wynik)




