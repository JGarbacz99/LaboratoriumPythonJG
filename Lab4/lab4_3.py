zwierzeta = []
for x in range (3):
    zwierze = input("Podaj nazwę zwierzęcia: ")
    zwierzeta.append(zwierze)
print(zwierzeta)
zwierzeta.sort()
print(zwierzeta)
print(zwierzeta[0], zwierzeta[-3: ])