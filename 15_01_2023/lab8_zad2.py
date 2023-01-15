
#zadanie 2

def sum_of_values(dict1):
    wynik = 0
    for i in dict1.values():
        wynik += i
    return wynik
dict1 = {'data1':10, 'data2':-4, 'data3':2}
dict2 = {'data1':15, 'data2':-2, 'data3':1, 'data4':87}
print(sum_of_values(dict1))
print(sum_of_values(dict2))