

# class AcousticDrums:

#     def __init__(self):
#         self.drum_material = "клён"
#         self.cymbal_material = "латунь"
#         self.quantity_of_drums = 5
#         self.quantity_of_cymbals = 4
#         self.brand = "Tama"
#
#     def get_acoustic_drums_info(self):
#         print(f"Материал барабанов: {self.drum_material}")
#         print(f"Материал тарелок: {self.cymbal_material}")
#         print(f"Количество барабанов: {self.quantity_of_drums}")
#         print(f"Количество тарелок: {self.quantity_of_cymbals}")
#         print(f"Бренд: {self.brand}")
#
#
# class ElectronicDrums:

#     def __init__(self):
#         self.drum_material = "кевлар"
#         self.cymbal_material = "кевлар + пластик"
#         self.quantity_of_drums = 4
#         self.quantity_of_cymbals = 4
#         self.brand = "Alesis"
#
#     def get_electronic_drums_info(self):
#         print(f"Материал барабанов: {self.drum_material}")
#         print(f"Материал тарелок: {self.cymbal_material}")
#         print(f"Количество барабанов: {self.quantity_of_drums}")
#         print(f"Количество тарелок: {self.quantity_of_cymbals}")
#         print(f"Бренд: {self.brand}")

#################################################################

class AcousticDrums:

    def __init__(self):
        self.drum_material = "клён"
        self.cymbal_material = "латунь"
        self.quantity_of_drums = 5
        self.quantity_of_cymbals = 4
        self.brand = "Tama"

    def get_drums_info(self):
        print(f"Материал барабанов: {self.drum_material}")
        print(f"Материал тарелок: {self.cymbal_material}")
        print(f"Количество барабанов: {self.quantity_of_drums}")
        print(f"Количество тарелок: {self.quantity_of_cymbals}")
        print(f"Бренд: {self.brand}")
        print(f"Акустические ударные установки - это настоящий звук и натуральные ощущения!")


class ElectronicDrums:

    def __init__(self):
        self.drum_material = "кевлар"
        self.cymbal_material = "кевлар + пластик"
        self.quantity_of_drums = 4
        self.quantity_of_cymbals = 4
        self.brand = "Alesis"

    def get_drums_info(self):
        print(f"Материал барабанов: {self.drum_material}")
        print(f"Материал тарелок: {self.cymbal_material}")
        print(f"Количество барабанов: {self.quantity_of_drums}")
        print(f"Количество тарелок: {self.quantity_of_cymbals}")
        print(f"Бренд: {self.brand}")
        print(f"Электронные ударные установки - это бесшумность и мобильность!")


drum_kit1 = AcousticDrums()
drum_kit2 = ElectronicDrums()

drum_catalog = [drum_kit1, drum_kit2]
for drums in drum_catalog:
    # drums.get_acoustic_drums_info
    drums.get_drums_info()  # Метод имеет одинаковое название в обоих классах, но его функции слегка разнятся
    print("================")
