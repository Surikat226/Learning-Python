# 1
a = 0

while a < 20:
    a = a+1
    print("Цикл выполнился", a, "раз(а)")
print("Цикл завершён")

print("-------------")

# 2
word_list = []
while len(word_list) < 5:
    inp = input()
    word_list.append(inp)
print(word_list)