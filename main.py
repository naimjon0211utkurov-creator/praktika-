
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__fuel = 0

    def refuel(self, litres):
        if litres > 0:
            self.__fuel += litres
            print(f"Заправлено {litres} литров")
        else:
            print("Количество топлива должно быть больше 0")

    def drive(self, km):
        fuel_needed = km * 0.1

        if self.__fuel >= fuel_needed:
            self.__fuel -= fuel_needed
            print(f"{self.brand} {self.model} проехала {km} км")
        else:
            print("Недостаточно топлива!")

    def info(self):
        return f"{self.brand} {self.model}, топливо: {self.__fuel} л"


# Создаём два объекта
car1 = Car("Daewoo", "Nexia 3")
car2 = Car("Chevrolet", "Cobalt")

# Проверяем методы первой машины
car1.refuel(12)
car1.drive(50)
print(car1.info())

print("--------------------")

# Проверяем методы второй машины
car2.refuel(20)
car2.drive(100)
print(car2.info())
