# Создаем класс Person 
class Person:
    # Конструктор класса Person
    def __init__(self, name, age):
        # Задаем имя
        self.name = name
        # Задаем возраст
        self.age = age

# Создаем класс Student, который идет от Person
class Student(Person):
    # Конструктор класса Student
    def __init__(self, name, age, student_id):
        # Вызываем конструктор класса (Person) для name и age
        super().__init__(name, age)
        # Добавляем уникальный id (идентификатор студента)
        self.id = student_id
    
    # Метод для строкового представления объекта (вызывается при print())
    def __str__(self):
        # Возвращаем строку с  подстановкой информацией о студенте
        return f"{self.name}, возраст: {self.age}, ID: {self.id}"

# Создаем класс Teacher, который идет от Person
class Teacher(Person):
    # Конструктор класса Teacher
    def __init__(self, name, age, subject):
        # Вызываем конструктор класса (Person)
        super().__init__(name, age)
        # Добавляем subject (предмет, который преподает учитель)
        self.subject = subject
        # Создаем пустой список students для хранения студентов преподавателя
        self.students = []
    
    # Метод для добавления студента
    def add_student(self, student):
        # Проверяем, есть ли студент уже в списке
        if student in self.students:
            print(f"Студент {student.name} уже есть в списке")
        else:
            # Добавляем студента в список
            self.students.append(student)
            print(f"Добавлен студент: {student.name}")
    
    # Метод для удаления студента
    def remove_student(self, student):
        # Проверяем, есть ли студент в списке
        if student in self.students:
            # Удаляем студента из списка
            self.students.remove(student)
            print(f"Удален студент: {student.name}")
        else:
            print(f"Студент {student.name} не найден")
    
    # Метод для отображения списка студентов
    def show_students(self):
        # Выводим заголовок с именем преподавателя
        print(f"\nСтуденты преподавателя {self.name}:")
        # Проверяем, есть ли студенты
        if not self.students:
            print("Нет студентов")
        # Перебираем всех студентов и выводим их имена
        for student in self.students:
            print(student.name)

# Пример использования классов
student1 = Student('Данилова Екатерина', 18, '284')
student2 = Student('Калашникова Ольга', 19, '999')

# Создаем преподавателя
teacher = Teacher('Наташа Петрова', 67, 'Русский')

# Добавляем студентов к преподавателю
teacher.add_student(student1)  # Добавится
teacher.add_student(student2)  # Добавится
teacher.add_student(student2)  # Не добавится (уже есть)

# Показываем список студентов
teacher.show_students()

# Удаляем студента
teacher.remove_student(student1)  # Удалится
teacher.remove_student(student1)  # Не удалится (уже удален)

# Снова показываем список студентов
teacher.show_students()
