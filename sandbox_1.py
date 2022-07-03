class A:
    def __init__(self):
        self.length = 20
        self.width = 5

    def show_info(self):
        print("Метод класса 'A'")
        print(f"Длина: {self.length}, ширина: {self.width}")


class B(A):
    def __init__(self):
        self.volume = 50

    def show_info(self):
        print("Метод класса 'B'")
        print(f"Объём: {self.volume}")


container = B()
# При вызове метода show_info() класса B
container.show_info()
