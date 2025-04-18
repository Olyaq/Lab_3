class Student:
    def __init__(self, name, surname, student_id):
        self.name=name
        self.surname=surname
        self.student_id=student_id
        self.grades=[]

    def __str__(self):
        return f"Student(name='{self.name}', surname='{self.surname}', student_id={self.student_id}, grades={self.grades})"
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id==other.student_id
        return False
    
    def __len__(self):
        return len(self.grades)
    
student1 = Student('Екатерина', 'Данилова', 9)
student1.grades = [5, 2, 4]
student2 = Student('Ольга', 'Калашникова', 9)
student2.grades = [3, 4, 5]
print(student1)  
print(student1 == student2)  
print(len(student1))  
