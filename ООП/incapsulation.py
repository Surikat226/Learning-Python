

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__breed = "Дворняга"
        self.__weight = 10

    def set_breed(self, breed):
        self.__breed = breed

    def get_breed(self):
        return self.__breed

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def __stand_up(self):
        print("Собака встала")

    def go_to_specific_place(self, dest_place):
        self.__stand_up()
        print(f"Собака пошла в место: {dest_place}")


if __name__ == '__main__':
    dog1 = Dog("Бобик", 7)

    dog1.name = "Маркс"  # Обращаясь напрямую к атрибуту класса, мы можем его переназначить
    dog1.go_to_specific_place("будка")  # Обращаемся напрямую к публичному методу
    # dog1.__stand_up  # Этот метод приватный, и мы не можем обратиться к нему извне

    # Это публичный атрибут, к которому обращаемся напрямую
    print(f"Имя собаки: {dog1.name}")
    # Это публичный атрибут, к которому обращаемся напрямую
    print(f"Возраст собаки: {dog1.age} лет.")


    # # Это приватный атрибут, который доступен только внутри класса. Мы не можем вызвать/изменить его извне так
    # print(f"Порода собаки: {dog1.__breed}")
    # # Это приватный атрибут, который доступен только внутри класса. Мы не можем вызвать/изменить его извне так
    # print(f"{dog1.__weight}")

    print("=====================")
    # Но на самом деле можем:
    print("Вызов приватного метода:")
    dog1._Dog__stand_up()