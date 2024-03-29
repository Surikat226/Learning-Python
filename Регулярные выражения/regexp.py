import re

text = """Множество ритмических рисунков, используемых нами сегодня, пришли именно из древности, в частности из
        музыкальных ритмов африканских племён. Старинный барабан был устроен практически так же, как и современный – он
        состоял из полой кадушки и натянутых с двух сторон мембран. Мембраны стягивались жилами зверей или веревками,
        с их помощью производилась настройка инструмента. В качестве мембран у некоторых индейских племён применяли
        для этого кожу с тела поверженного врага, но к счастью теперь мы используем пластики из полимерных соединений.
        Барабанные палочки появились значительно позже — изначально звук барабана извлекали руками. Турецкие племена
        первыми использовали для игры тарелки. Педаль для большого барабана была изобретена Уильямом Ф. Людвигом в 1909
        году, а понятие «кардан» впервые запатентовала фирма DW. Производители Эванс и Ремо (Lorem ipsum dolor sit
        amet) одни из первых 88005553535 начали Excepteur sint occaecat cupidatat применять синтетические пластики.
        Впоследствии появилось большое разнообразие ударных инструментов в различных But I must explain to you how all
        this mistaken странах. Но откуда появилась ударная установка, которую мы знаем сегодня?
        Мууууууууууууу! Муууууууууууууууууууу! И ещё раз - му!"""


# Символьные классы []
#1 Найти только латиницу
match1 = re.findall(r"[A-Za-z]", text)
print("match1:", match1)

#2 Найти только кириллицу
match2 = re.findall(r"[А-Яа-яЁё]", text)
print("match2:", match2)

#3 Найти цифры
match3 = re.findall(r"[\d]", text)  # \d (digit) - аналог [0-9]
print("match3:", match3)

#4 Найти всё, кроме: цифр (\d), не-слов (\W) и кириллических букв
match4 = re.findall(r"[^\d\WА-Яа-яЁё]", text)  # \W (non-word) - найти все "не-слова"
print("match4:", match4)

#5 Найти словосочетание "Эванс и Ремо" и заменить его на "Tama"
match5 = re.sub(r"Эванс и Ремо", "Tama", text)
print("match5:", match5)

# Квантификаторы {}
#6 Найти от 5 до 8 повторений буквы "у" в тексте
match6 = re.findall(r"у{5,8}", text)
print("match6:", match6)

