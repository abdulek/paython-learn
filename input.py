name = input("Enter your name")
print(name)
try:
    number = int(input("Enter a number"))
    print(number)
except TypeError:
    print(TypeError)


