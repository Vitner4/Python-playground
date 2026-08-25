letters = list("Hello world! i'm pro programmer!")
print(letters)      # ['H', 'e', 'l', 'l', 'o']

char = "pHaD"
charList = list(char)

for i in letters:
    for j in charList:
        if i.lower() == j.lower():
            print(f"\"{i}\" is found!")