
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"{self.name} say: Привет, я {self.name}!")

    def say_your_age(self):
        print(f"{self.name} say: Мне {self.age}")

user1 = User("Nik", 23)
user2 = User("Kane", 12)

user1.say_hello()
user2.say_your_age()


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} едет!")

car1 = Car("Toyota", "Camry")
car1.drive()