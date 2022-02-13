# обычная функция
def calc_sum(a, b):
    c = a+b
    return c
print(calc_sum(10, 20))

# лямбда-функция
l = lambda x, y: x+y
print(l(10, 20))


listik = [1, 2, "Привет", lambda x, y: print(x+y), 4.96]
print(listik[3](listik[0], listik[4]))