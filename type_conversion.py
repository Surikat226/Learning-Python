print("Строка в число:")
str_number = "12"
int_number = int(str_number)
print(type(str_number))
print(type(int_number))

print("=====================")

print("Двоичное число в десятичное:")
converted_double = int("11111111", 2)
print(converted_double)

print("=====================")

print("Десятичное число в двоичное:")
int_number2 = 15
int_to_double = bin(int_number2)
print(int_to_double)

print("=====================")

print("Десятичное число в шестнадцатеричное:")
int_number3 = 30
int_to_hex = hex(int_number3)
print(int_to_hex)

print("=====================")

print("Преобразование аргументов в список:")
some_string = "Строка"
print(list(some_string))

print("=====================")

"Преобразование аргументов в кортеж:"
another_string = "Строка 2"
print(tuple(another_string))