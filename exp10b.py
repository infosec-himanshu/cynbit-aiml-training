student={}
n=int(input("enter the number of students"))
for i in range(n):
    name=(input("enter the name"))
    marks=float(input("enter the marks"))
    student[name]=marks
print("60+ topppers")
for name,marks in student.items():
    if marks>60:
        print(name,":",marks)