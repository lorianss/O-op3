from abc import ABC, abstractmethod
import math

# Абстрактный базовый класс Figure
class Figure(ABC):
    @abstractmethod
    def area(self):
        """Вычисление площади фигуры."""
        pass

    @abstractmethod
    def perimeter(self):
        """Вычисление периметра фигуры."""
        pass

    @abstractmethod
    def input_data(self):
        """Ввод данных фигуры."""
        pass

    @abstractmethod
    def output_data(self):
        """Вывод данных фигуры."""
        pass


# Производный класс Rectangle (прямоугольник)
class Rectangle(Figure):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def input_data(self):
        self.width = float(input("Введите ширину прямоугольника: "))
        self.height = float(input("Введите высоту прямоугольника: "))

    def output_data(self):
        print(f"Прямоугольник: ширина = {self.width}, высота = {self.height}")
        print(f"Площадь: {self.area()}, Периметр: {self.perimeter()}")


# Производный класс Circle (круг)
class Circle(Figure):
    def __init__(self, radius=0):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def input_data(self):
        self.radius = float(input("Введите радиус круга: "))

    def output_data(self):
        print(f"Круг: радиус = {self.radius}")
        print(f"Площадь: {self.area():.2f}, Периметр: {self.perimeter():.2f}")


# Производный класс Trapezium (трапеция)
class Trapezium(Figure):
    def __init__(self, base1=0, base2=0, height=0, side1=0, side2=0):
        self.base1 = base1
        self.base2 = base2
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return (self.base1 + self.base2) * self.height / 2

    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2

    def input_data(self):
        self.base1 = float(input("Введите длину первого основания трапеции: "))
        self.base2 = float(input("Введите длину второго основания трапеции: "))
        self.height = float(input("Введите высоту трапеции: "))
        self.side1 = float(input("Введите длину первой боковой стороны: "))
        self.side2 = float(input("Введите длину второй боковой стороны: "))

    def output_data(self):
        print(f"Трапеция: основание1 = {self.base1}, основание2 = {self.base2}, "
              f"высота = {self.height}, сторона1 = {self.side1}, сторона2 = {self.side2}")
        print(f"Площадь: {self.area():.2f}, Периметр: {self.perimeter():.2f}")


# Функция вывода, демонстрирующая виртуальный вызов
def display_figure_info(figure: Figure):
    figure.output_data()


# Вызывающая программа
if __name__ == '__main__':
    # Создание объектов производных классов
    rectangle = Rectangle()
    circle = Circle()
    trapezium = Trapezium()

    print("Введите данные для прямоугольника:")
    rectangle.input_data()

    print("\nВведите данные для круга:")
    circle.input_data()

    print("\nВведите данные для трапеции:")
    trapezium.input_data()

    print("\nИнформация о фигурах:")
    display_figure_info(rectangle)
    print()
    display_figure_info(circle)
    print()
    display_figure_info(trapezium)