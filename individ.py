# Базовый класс Car
class Car:
    def __init__(self, brand: str, cylinders: int, power: int):
        self._brand = brand  # Торговая марка
        self._cylinders = cylinders  # Число цилиндров
        self._power = power  # Мощность

    # Геттер для торговой марки
    @property
    def brand(self):
        return self._brand

    # Сеттер для торговой марки
    @brand.setter
    def brand(self, new_brand: str):
        self._brand = new_brand

    # Метод для изменения мощности
    def change_power(self, new_power: int):
        if new_power > 0:
            self._power = new_power
        else:
            print("Мощность должна быть положительным числом.")

    # Метод для вывода информации о машине
    def display_info(self):
        print(f"Марка: {self._brand}, Цилиндры: {self._cylinders}, Мощность: {self._power} л.с.")


# Производный класс Lorry (грузовик)
class Lorry(Car):
    def __init__(self, brand: str, cylinders: int, power: int, capacity: float):
        super().__init__(brand, cylinders, power)  # Вызов конструктора базового класса
        self._capacity = capacity  # Грузоподъемность кузова

    # Геттер для грузоподъемности
    @property
    def capacity(self):
        return self._capacity

    # Сеттер для грузоподъемности
    @capacity.setter
    def capacity(self, new_capacity: float):
        if new_capacity > 0:
            self._capacity = new_capacity
        else:
            print("Грузоподъемность должна быть положительным числом.")

    # Переопределение метода для вывода информации о грузовике
    def display_info(self):
        super().display_info()  # Вызов метода базового класса
        print(f"Грузоподъемность: {self._capacity} тонн")


# Демонстрация возможностей классов
if __name__ == '__main__':
    # Создание объекта базового класса Car
    car = Car("Toyota", 4, 150)
    print("Информация о машине:")
    car.display_info()

    # Изменение мощности машины
    car.change_power(180)
    print("\nПосле изменения мощности машины:")
    car.display_info()

    # Переназначение марки машины
    car.brand = "Honda"
    print("\nПосле изменения марки машины:")
    car.display_info()

    # Создание объекта производного класса Lorry
    lorry = Lorry("Volvo", 6, 300, 10)
    print("\nИнформация о грузовике:")
    lorry.display_info()

    # Изменение грузоподъемности грузовика
    lorry.capacity = 12
    print("\nПосле изменения грузоподъемности грузовика:")
    lorry.display_info()

    # Переназначение марки грузовика
    lorry.brand = "Scania"
    print("\nПосле изменения марки грузовика:")
    lorry.display_info()