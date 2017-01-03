def addition(a, b):
    return (a + b)


def multiply(a, b):
    return a * b


def substraction(a, b):
    return (a - b)


def division(a, b):
    if(b == 0):
        print("Invalid value of b ")
        return
    return a / b


print(addition(2, 4))
print(multiply(10, 4))
print(substraction(100, 70))
print(division(100, 10))
print(division(20, 0))
