class Person:
    def __init__(self,age,name):
        self.name=name
        self.age=age
    
class Student(Person):
        def __init__(self,rollno,marks,age,name):
             super().__init__(name,age)
             self.rollno=rollno
             self.marks=marks
        
        def display(self):
            print("name",self.name)
            print("age",self.age)
            print("roll",self.rollno)
            print("marks",self.marks)
s= Student(2,100,20,"boss")
s.display()