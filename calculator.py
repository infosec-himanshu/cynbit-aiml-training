def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

try:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    
    print(f"Addition: {add(x, y)}")
    print(f"Subtraction: {sub(x, y)}")
    print(f"Multiplication: {mul(x, y)}")
    print(f"Division: {div(x, y)}")
except ValueError:
    print("Please enter valid numeric numbers.")