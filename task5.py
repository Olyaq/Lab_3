# Создаём класс Student 
class Student:
    # Конструктор класса, вызывается при создании нового объекта
    def __init__(self, name, surname, student_id):
        self.name = name        # Сохраняем имя студента
        self.surname = surname  # Сохраняем фамилию студента
        self.student_id = student_id  # Сохраняем ID студента
        self.grades = []        # Создаём пустой список для оценок

    # Метод для строкового представления (вызывается при print())
    def __str__(self):
        return f"Student(name='{self.name}', surname='{self.surname}', student_id={self.student_id}, grades={self.grades})"
    
    # Метод для сравнения объектов 
    def __eq__(self, other):
        if isinstance(other, Student):  # Проверяем, что other - тоже Student
            return self.student_id == other.student_id  # Сравниваем по ID
        return False  # Если other не Student, возвращаем False
    
    # Метод для получения длины (вызывается функцией len())
    def __len__(self):
        return len(self.grades)  # Возвращаем количество оценок
    
# Создаём первый объект студента
student1 = Student('Екатерина', 'Данилова', 9)
student1.grades = [5, 2, 4]  # Устанавливаем оценки 

# Создаём второй объект студента
student2 = Student('Ольга', 'Калашникова', 9)
student2.grades = [3, 4, 5]  # Устанавливаем оценки

# Выводим информацию о первом студенте 
print(student1)  
# Сравниваем студентов 
print(student1 == student2)  
# Получаем количество оценок первого студента 
print(len(student1))
