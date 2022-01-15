### Способы создания списков
list1 = []
list2 = list()
print(type(list1))
print(type(list2))

print()

### Заполнение списков элементами
int_list = [1, 3, 5]
string_list = ["я", "люблю", "дуть", "плюхи"]

some_var = "тут что-то есть"
mixed_list = ["Путин", 20, 11.5, some_var]

nested_list = [int_list, string_list, mixed_list]

print("Это список с числами:", int_list)
print("Это список со строками:", string_list)
print("Это список со смешанными элементами:", mixed_list)
print("Это список со списками:", nested_list)

print()

### Комбинирование списков
combined_list = string_list + int_list + mixed_list
print("Это комбинированный список, который складывает наши списки вместе:", combined_list)

print()

### Сортировка списка
chaotic_list = [2, 5, 0, 65, 101, 34, 9]
chaotic_list.sort()
print("Отсортированный список:", chaotic_list)
# но если попытаться присвоить наш список какой-либо переменной и применить к ней метод сортировки,
# то получим "None" (что равносильно "Null" в других языках), т.к. список сортируется на изначальном месте:
sorted_list = chaotic_list.sort()
print("Попытались применить метод сортировки к переменной и получили:", sorted_list)

print()

### Срез списка
random_list = [1, "двадцать", 22.8, "Нэвэльный", "ра-та-та-та", 16, 100]
three_elements = random_list[2:5]
print(three_elements)
# или
print(random_list[2:5])