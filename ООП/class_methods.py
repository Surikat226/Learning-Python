

class WitcherClass:

    CLASS_NAME = "WitcherClass"
    WITCHER_NAME = "Геральт"
    WITCHER_HORSE = "Плотва"

    def some_standard_method(self):
        print(f"Это метод экземпляра класса {self.CLASS_NAME}!")

    # @classmethod вместо первого параметра "self" имеет параметр "cls", поэтому такой метод МОЖЕТ ссылаться
    # только на атрибуты класса и НЕ МОЖЕТ ссылаться на экземпляры класса, т.е. менять их состояние
    @classmethod
    def some_class_method(cls):
        print(f"Это \"@classmethod\" класса {cls.CLASS_NAME}!")

    # @staticmethod никак не связан ни с атрибутами и методами класса, ни с экземплярами данного класса
    # Он является неким методом, который косвенно (тематически) связан с текущим классом, но прямого отношения
    # к нему он не имеет, и никак не может влиять на атрибуты класса
    @staticmethod
    def some_static_method():
        print(f"Это \"@staticmethod\" класса \"{WitcherClass.CLASS_NAME}\"!")


witcher = WitcherClass()

witcher.some_standard_method()
witcher.some_class_method()
witcher.some_static_method()
WitcherClass.some_static_method()