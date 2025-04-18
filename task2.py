class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.id = student_id
    
    def __str__(self):
        return f"{self.name}, возраст: {self.age}, ID: {self.id}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.students = []
    
    def add_student(self, student):
        if student in self.students:
            print(f"Студент {student.name} уже есть в списке")
        else:
            self.students.append(student)
            print(f"Добавлен студент: {student.name}")
    
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Удален студент: {student.name}")
        else:
            print(f"Студент {student.name} не найден")
    
    def show_students(self):
        print(f"\nСтуденты преподавателя {self.name}:")
        if not self.students:
            print("Нет студентов")
        for student in self.students:
            print(student.name)

# Пример использования
student1 = Student('Данилова Екатерина', 18, '284')
student2 = Student('Калашникова Ольга', 19, '999')

teacher = Teacher('Светлана Ивановна', 45, 'Математика')

teacher.add_student(student1)
teacher.add_student(student2)
teacher.add_student(student2)  # Попытка добавить повторно

teacher.show_students()

teacher.remove_student(student1)
teacher.remove_student(student1)  # Попытка удалить повторно

teacher.show_students()
