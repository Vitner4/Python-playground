from typing import Protocol


class Logger(Protocol):
    def log(self, message: str) -> None:
        ...

class FileLogger:
    def log(self, message: str) -> None:
        print(f"Запись в файл: {message}")

class TelegramLogger:
    def log(self, message: str) -> None:
        print(f"Telegram: {message}")

class UserService:
    def __init__(self, logger: Logger):
        self.logger = logger

    def create_user(self, name: str) -> None:
        print(f"Создан пользователь: {name}")
        self.logger.log(f"Пользователь {name} создан")

file_logger = FileLogger()
telegram_logger = TelegramLogger()

service1 = UserService(file_logger)
service2 = UserService(telegram_logger)

service1.create_user("@Alex23")
service2.create_user("@Sage")



class Storage(Protocol):
    def save(self, data: str) -> None:
        ...

class FileStorage:
    def save(self, data: str) -> None:
        print(f"\"{data}\" сохранено в файл!")

class DataBaseStorage:
    def save(self, data: str) -> None:
        print(f"\"{data}\" сохранено БД!")

def save_data(storage: Storage, data: str):
    storage.save(data)

file = FileStorage()
db = DataBaseStorage()

save_data(file, "I love Tokio!")
save_data(db, "Hamburger")



class Car(Protocol):
    def drive(self, car_name: str) -> bool:
        ...

class Toyota(Car):
    def drive(self, car_name: str) -> bool:
        print(f"{car_name} едет!")
        return True

def driving(car: Car, car_name: str):
    return car.drive(car_name)

toyota = Toyota()
toyota_driving = driving(toyota, "Toyota")

print("Driving status:", toyota_driving)

