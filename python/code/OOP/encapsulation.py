
class Bank:
    def __init__(self, name, id, balance):
        self._name = name # _name - маркер для разработчиков, обозначение внутреннего (сокрытого) атрибута (поля)
        self.__id = id # __id (_Bank__id) - name mangling (преобразование атрибута для предотвращения случайного вызова)
        self._balance = balance

    # Getter
    @property
    def balance(self):     
        return self._balance

    @balance.setter
    def balance(self, value):
        # Условие работы с сокрытым полем
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным!")
        
        self._balance = value


# user1 = Bank("Nik", 44567, 1500)
# print(user1.balance) # getter
# user1.balance = 1000 # setter
# print(user1.balance)


class User:
    def __init__(self, password):
        self.password = password # проверяем пароль в методе setter перед записью

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("Пароль должен быть не менее 8 символов!")
        
        self._password = value


user = User("12345678")
print(user.password)
user.password = "4fg46hd86"
print(user.password)