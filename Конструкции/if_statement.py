# 1
print("Введите два числа")
a = int(input())
b = int(input())

if a+b <= 100:
    print("Вы ввели числа, в сумме не превышающие 100")
else:
    print("Вы довен")


print("--------------")


random_list = [1, "Здрасьте", 33.7, "Покеда"]
if 1 in random_list:
    print("Элемент \"1\" входит в список")
else:
    print("Элемент \"1\" не входит в список")