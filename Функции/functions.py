### Создание и вызов функции
def no_agrs_func():
    print("Хаюшки!")
no_agrs_func()

print("----------------")

def location_info(country, region, city):
    print("Страна:", country)
    print("Регион:", region)
    print("Город:", city)

location_info("Россия", "Краснодарский край", "Краснодар")

print("----------------")
print("----------------")

### Необязательные аргументы
def human_info(name, surname, age=24, gender="Мужской"):
    print(f"Имя: {name}")
    print(f"Фамилия: {surname}")
    print(f"Возраст: {age}")
    print(f"Пол: {gender}")

human_info("Артём", "Овчинников")

print("----------------")
print("----------------")

### return в функциях
def calc(x, y):
    z = x + y
    return z

a = 50
c = a + calc(20, 30)
print(c)

print("----------------")
print("----------------")

### Позиционные и именованные аргументы
# В Питоне существует два вида аргументов: позиционные и именованные.
# Разница в том, что позиционные аргументы указываются в строгом порядке,
# а при указании именованных можно нарушать порядок их указания. Например:
def pos_named_args_func(bird, dog, cat):
    print(bird)
    print(dog)
    print(cat)
pos_named_args_func("Чайка", "Дворовый пёс", "Сиамский")
pos_named_args_func(cat="Сиамский", bird="Чайка", dog="Дворовый пёс")

print("----------------")
print("----------------")

### Переменное кол-во аргументов в функции (*args и **kwargs)
# *args используются для передачи рандомного кол-ва позиционных аргументов
def enter_args(*names):
    for name in names:
        print(f"Ты {name}?")

enter_args("Лёша", "Петя", "Саша", "Вася")

# **kwargs используются для передачи именованных аргументов
def show_pets(**pet):
    for key, value in pet.items():
        print(f"Животное - {key}, порода - {value}")
show_pets(Кот="египетский", Пёс="облезший", Попуга="заебал")