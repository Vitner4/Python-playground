myList = ["hello", 1]

myList.append("world")
myList.extend(["Bob", "Tom"])
myList.insert(len(myList), "!")

print(myList)

element = myList.index("Bob")
print("index of Bob is", element)
myList.pop(element)

print(myList)

myList.pop()

print(myList)

myList.remove("Tom")

print(myList)

del myList[1]

print(myList)