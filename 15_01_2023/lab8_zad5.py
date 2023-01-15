def dodawanie(x, y):
    return x+y
def odejmowanie(x, y):
    return x-y
def mnozenie(x, y):
    return x-y
def dzielenie(x, y):
    if y != 0:
        return x/y
    else: return None

kalkulator={'+': dodawanie, '-': odejmowanie, '*': mnozenie, '/': dzielenie}
d="+"
L1 = 2
L2 = 3

print(kalkulator[d](L1, L2))

