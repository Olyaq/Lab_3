class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            print("Ошибка! Оценка должна быть от 0 до 10")
    
    def get_average(self):
        return sum(self.grades)/len(self.grades) if self.grades else 0
    
    def show_info(self):
        print(f"Студент: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Оценки: {self.grades}")
        print(f"Средний: {self.get_average():.1f}")


# Пример использования
student = Student("Ольга Калашникова", "999")
student.add_grade(5)
student.add_grade(6)
student.add_grade(8)
student.show_info()
