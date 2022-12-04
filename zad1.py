values = [10,20,30]
keys = ['ten', 'twenty', 'thirty']

# print(list(zip(keys, values)))
# D1= dict(zip(keys, values))
# D1 = {}
# for i in range(len(keys)):
#    D1[keys[i]] = values[i]


D1 = { keys[i]:values[i] for i in range(len(keys))}
print("D1 =", D1)

D2 = dict(thirty = 30, forty = 40, fifty = 50)
print("D2 =", D2)

D3 = D1.copy()
D3.update(D2)

print("D3=", D3)