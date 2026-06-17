name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

print("\n--- Student Profile ---")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"City : {city}")
print("-----------------------")

try:
    marks = int(input("Enter your marks (0-100): "))
    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter a value between 0 and 100.")
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