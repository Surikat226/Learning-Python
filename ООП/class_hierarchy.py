

class GameUnit:

    def __init__(self, nation):
        self._nation = nation


class Vehicle(GameUnit):

    def __init__(self, nation, vehicle_type):
        super().__init__(nation)
        self._vehicle_type = vehicle_type


class Tank(Vehicle):

    def __init__(self, nation, vehicle_type, tank_name, tank_gun):
        super().__init__(nation, vehicle_type)
        self.__tank_name = tank_name
        self.__tank_gun = tank_gun

    def get_info(self):
        print(f"Нация: {self._nation}")
        print(f"Тип транспорта: {self._vehicle_type}")
        print(f"Название танка: {self.__tank_name}")
        print(f"Пушка: {self.__tank_gun}")


class Helicopter(Vehicle):

    def __init__(self, nation, vehicle_type, helicopter_role, helicopter_name, helicopter_weapon):
        super().__init__(nation, vehicle_type)
        self.__helicopter_role = helicopter_role
        self.__helicopter_name = helicopter_name
        self.__helicopter_weapon = helicopter_weapon

    def get_info(self):
        print(f"Нация: {self._nation}")
        print(f"Тип транспорта: {self._vehicle_type}")
        print(f"Название вертолёта: {self.__helicopter_name}")
        print(f"Роль: {self.__helicopter_role}")
        print(f"Вооружение: {self.__helicopter_weapon}")


class Infantry(GameUnit):

    def __init__(self, nation, specialty):
        super().__init__(nation)
        self._infantry_specialty = specialty


class Sniper(Infantry):

    def __init__(self, nation, specialty, weapon):
        super().__init__(nation, specialty)
        self.__weapon = weapon

    def get_info(self):
        print(f"Нация: {self._nation}")
        print(f"Специальность пехотинца: {self._infantry_specialty}")
        print(f"Вооружение: {self.__weapon}")


tiger_tank = Tank("Германия", "Танк", "Tiger P", "88-мм KwK 36 L/56")
tiger_tank.get_info()
print("=====================")
ka_52 = Helicopter("Российская Федерация", "Вертолёт", "Атакующий вертолёт",
                   "КА-52 \"Аллигатор\"", "ПТРК \"Штурм-ВУ\", \"НАР С-52\"")
ka_52.get_info()
print("=====================")
alexei_novikov = Sniper("Российская Федерация", "Снайпер", "СВД")
alexei_novikov.get_info()
