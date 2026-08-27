
class Car:
    # Один общий интерфейс 
    def move(self):
        print("Машина едет") # разная реализация 

class Plane:
    # Один общий интерфейс 
    def move(self):
        print("Самолёт летит") # разная реализация 

class Boat:
    # Один общий интерфейс 
    def move(self):
        print("Лодка плывёт") # разная реализация 

# Список безымянных объектов класса
objects = [
    Car(),
    Plane(),
    Boat()
]

# Демонстрация полиморфизма
for obj in objects:
    obj.move()