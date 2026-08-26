
class User:
    # Метод инициализации объекта
    def __init__(self, name: str, age: int):
        self.name = name # атрибут (поле) объекта
        self.age = age # атрибут (поле) объекта

    # Метод класса
    def say_hello(self):
        print(f"{self.name} say: Привет, я {self.name}!")

    # Метод класса
    def say_your_age(self):
        print(f"{self.name} say: Мне {self.age}")

user1 = User("Nik", 23) # создание объекта класса User и определение атрибутов
user2 = User("Kane", 12) # создание другого объекта класса User и определение атрибутов

user1.say_hello() # вызов метода
user2.say_your_age() # вызов метода


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} едет!")

car1 = Car("Toyota", "Camry")
car1.drive()