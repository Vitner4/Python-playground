n = 80

def func():

    global n
    n = 90

    def localFunc():

        n = 40

        def doubleLocalFunc():
            global n
            n = 100

        print(n)
        doubleLocalFunc()
    
    localFunc()
    print(n)

print(n)
func()

