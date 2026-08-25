def money_generator():
    dollar = 1

    while True:
        yield dollar
        dollar += 1

money = money_generator()
n = 100

for i in range(n):
    print(next(money))