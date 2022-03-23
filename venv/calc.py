def add():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a + b)

def substraction():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a - b)

def multiply():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a * b)

def divide():
    a = float(input("Enter a number. "))
    b = float(input("Enter another number. "))
    print(a / b)

operation = input("Please type +, -, *, or / ")
if operation == '+':
    add()
elif operation == '-':
    substraction()
elif operation == '*':
     multiply()
elif operation == '/':
    divide()
else:
    print("That operation is not available. ")

add()
substraction()
multiply()
divide()


