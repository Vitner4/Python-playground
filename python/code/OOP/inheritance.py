
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} ест")

    def make_sound(self):
        print(f"{self.name} издаёт какой-то звук")


class Dog(Animal): # вид наследования класса Animal подклассом Dog 
    def __init__(self, name, age):
        super().__init__(name) # вызываем __init__ родительского класса
        self.age = age

    def bark(self):
        print(f"{self.name}: Гав!")

    # Переопределенный метод из класса Animal
    def make_sound(self):
        print(f"{self.name} гавкает!")


class Cat(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name)
        self.age = age

    def make_sound(self):
        print(f"{self.name} мяукает!")

cat = Cat("Neko", 5)
cat.make_sound()
cat.eat()