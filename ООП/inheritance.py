print("Данные родительского класса:")
print("----------------------------")


class Character:

    def __init__(self, name):
        self.name = name
        self.gender = "Мужчина"
        self.health = 100
        self.attack = 10
        self.armor = 0
        self.char_class = "Воин"

    def choose_char_gender(self, gender):
        if (gender == "Мужчина") or (gender == "Женщина"):
            self.gender = gender
        else:
            raise AttributeError(f"Выберите пол: \"Мужчина\" или \"Женщина\"")

    def choose_char_class(self, char_class):
        if (char_class == "Воин") or (char_class == "Маг") or (char_class == "Охотник"):
            self.char_class = char_class
            print(f"Вы выбрали класс: {char_class}")
        else:
            raise AttributeError(f"Выберите класс: \"Воин\", \"Маг\" или \"Охотник\"")

    def show_char_info(self):
        print(f"Имя персонажа: {self.name}")
        print(f"Пол: {self.gender}")
        print(f"Здоровье: {self.health} HP")
        print(f"Атака: {self.attack}")
        print(f"Броня: {self.armor}")
        print(f"Класс: {self.char_class}")


char1 = Character("random_nickname43986742")
char1.show_char_info()

print("================================")
print("Данные дочернего класса:")
print("----------------------------")


class Mage(Character):

    def __init__(self, name):
        super().__init__(name)  # Наследуем атрибуты метода __init__() из родительского класса
        # Добавляем атрибуты, относящиеся к классу "Маг"
        self.mana = 50
        self.char_class = "Маг"
        self.mage_subclass = "Просветитель"
        self.weapon = "Простой посох огня"

    def show_char_info(self):
        super().show_char_info()  # Наследуем атрибуты метода show_char_info() из родительского класса
        # Добавляем печать атрибутов, которые мы добавили в __init__() класса Mage
        print(f"Подкласс: {self.mage_subclass}")
        print(f"Оружие: {self.weapon}")
        print(f"Количество маны: {self.mana}")

    def choose_mage_subclass(self, mage_subclass):
        if (mage_subclass == "Просветитель") or (mage_subclass == "Призыватель") or (mage_subclass == "Некромант"):
            self.mage_subclass = mage_subclass
        else:
            raise AttributeError(f"Выберите подкласс: \"Просветитель\", \"Призыватель\" или \"Некромант\"")

    def choose_mage_weapon(self, weapon):
        if (weapon == "Простой посох огня") or (weapon == "Книга древних"):
            self.weapon = weapon
        else:
            raise AttributeError(f"Выберите оружие: \"Простой посох огня\" или \"Книга древних\"")


mage1 = Mage("Ubivatelnitsa1488")
mage1.choose_char_gender("Женщина")
mage1.choose_mage_weapon("Книга древних")
mage1.choose_mage_subclass("Призыватель")
mage1.show_char_info()
