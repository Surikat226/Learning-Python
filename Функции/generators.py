

# Функция-генератор - функция, которая возвращает не весь результат выполнения функции, а возвращает
# его по частям, сохраняя предыдущее состояние функции после её выполнения.
# Генератор вызывается методом next(), а код генератора выполнется до первого попавшегося yield (аналог return).
# При повторном вызове генератора через next() код выполняется уже после yield до тех пор, пока не встретится
# новый yield.
def example_generator(final_number):
    while final_number != 0:
        print(f"Обратный отсчёт: {final_number}")
        yield final_number
        final_number -= 1


gen = example_generator(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def example_generator_2(name, surname, age, gender):
    print(f"Тебя зовут {name}")
    yield name

    print(f"Твоя фамилия - {surname}")
    yield surname

    print(f"Тебе {age} лет")
    yield age

    print(f"Твой пол - {gender}")
    yield gender

gen_2 = example_generator_2("Артём", "Овчинников", 24, "мужской")
print(next(gen_2))
print(next(gen_2))
print(next(gen_2))
print(next(gen_2))