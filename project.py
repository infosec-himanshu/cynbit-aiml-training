def get_percentage(student):
    return student["percentage"]
def main():
    students = []
    while True:
        try:
            num_students = int(input("How many students do you want to analyze? "))
            if num_students > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    for i in range(num_students):
        name = input(f"\nEnter name of student {i+1}: ")
        while True:
            marks_str = input("Enter marks for 5 subjects separated by a space: ")
            marks_list = marks_str.split()
            if len(marks_list) != 5:
                print("Error: You must enter exactly 5 marks.")
                continue
            try:
                marks = [float(m) for m in marks_list]
                is_valid = True
                for m in marks:
                    if m < 0 or m > 100:
                        is_valid = False
                        break
                if is_valid:
                    break 
                else:
                    print("Error: Marks must be between 0 and 100.")
            except ValueError:
                print("Error: Please enter valid numbers.")
        total = sum(marks)
        percentage = total / 5
        if percentage >= 80:
            performance = "Excellent"
        elif percentage >= 50:
            performance = "Average"
        else:
            performance = "Poor"
        student = {
            "name": name,
            "marks": marks,
            "total": total,
            "percentage": percentage,
            "performance": performance
        }
        students.append(student)
    filename = "students.txt"
    print(f"\nSaving student data to '{filename}'...")
    with open(filename, "w") as file:
        for s in students:
            marks_str = ",".join(str(m) for m in s["marks"])
            line = f"{s['name']},{marks_str},{s['total']},{s['percentage']},{s['performance']}\n"
            file.write(line)
    loaded_students = []
    print(f"Reading student data from '{filename}'...")
    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) == 9: 
                loaded_students.append({
                    "name": data[0],
                    "total": float(data[6]),
                    "percentage": float(data[7]),
                    "performance": data[8]
                })
    loaded_students.sort(key=get_percentage, reverse=True)

    print("\n" + "="*30)
    print("        TOP STUDENTS")
    print("="*30)
    top_allowed = min(3, len(loaded_students))
    
    for i in range(top_allowed):
        s = loaded_students[i]
        print(f"Rank {i+1}: {s['name']}")
        print(f"  Percentage : {s['percentage']}%")
        print(f"  Performance: {s['performance']}")
        print("-" * 30)

if __name__ == "__main__":
    main()
