a = (1, 3, 5, 7)
b = ["раз", "два", "три", "четыре"]
c = {"Имя": "Григорий", "Отчество": "Даунович", "Фамилия": "Васечкин"}
print(type(a))
print(type(b))
print(type(c))

print("------------")

class Electronics:
    def __init__(self):
        self.item_type = "Technica"
        self.item_rarity = "Rare"


class TV(Electronics):
    diag = "20 inches"
    price = "$200"

samsung = TV()
print(samsung.__dict__)