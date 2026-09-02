from abc import ABC, abstractmethod 
# ABC (Abstract Base Class) — базовый класс для создания
# абстрактных классов в Python.

class Shape(ABC):
    # Абстрактный метод
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        print("Площадь круга...")


class Rectangle(Shape):
    def area(self):
        print("Площадь прямоугольника...")

circle = Circle()
rectangle = Rectangle()

circle.area()
rectangle.area()