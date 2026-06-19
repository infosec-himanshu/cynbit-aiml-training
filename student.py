name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

print("\n--- Profile Summary ---")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"City : {city}")
print("\n")

try:
    marks = int(input("Enter your marks (0-100): "))
    if marks < 0 or marks > 100:
        print("Invalid marks!")
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: Fail")
except ValueError:
    print("Please enter a valid numeric number.")

print("\n")

try:
    num = int(input("Enter a number to generate its table: "))
    print(f"\nMultiplication Table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
except ValueError:
    print("Please enter a valid number.")