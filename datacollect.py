students = []

for i in range(3):
    print(f"Enter details for Student {i+1}:")
    name = input("Name: ")
    age = input("Age: ")
    city = input("City: ")
    
    student_dict = {
        "name": name,
        "age": age,
        "city": city
    }
    students.append(student_dict)
    print("-" * 20)

print("\n--- All Student Records ---")
for student in students:
    print(f"Name: {student['name']} | Age: {student['age']} | City: {student['city']}")