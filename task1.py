class Student: # Создаем класс Student
    # Определяем метод __init__, который вызывается при создании нового объекта класса
    # self - ссылка на текущий класса
    # name - имя студента, student_id - идентификатор студента
    def __init__(self, name, student_id):
        self.name = name    # Присваиваем переданное имя name объекта
        self.student_id = student_id  #
        self.grades = []   # Создаем пустой список grades для хранения 
    
    # Метод для добавления оценки студента
    def add_grade(self, grade):
        if 0 <= grade <= 10:   # Проверяем, что оценка находится в можно диапазоне (от 0 до 10)
            self.grades.append(grade)  # Если оценка подошла, добавляем ее в список grades
        else:
            print("Ошибка! Оценка должна быть от 0 до 10")   # Если оценка не подошла, выводим сообщение об ошибке
    
    # Метод для вычисления среднего балла студента
    def get_average(self):
        # Если список оценок не пустой, возвращаем среднее арифметическое
        return sum(self.grades)/len(self.grades) if self.grades else 0 
    
    # Метод для вывода информации о студенте
    def show_info(self):
        print(f"Студент: {self.name}")  # Выводим имя
        print(f"ID: {self.student_id}") # Выводим Id 
        print(f"Оценки: {self.grades}") # Выводим список оценок
        print(f"Средний: {self.get_average():.1f}")  # Выводим средний балл, до 1 знака после запятой


# Пример использования класса Student
student = Student("Ольга Калашникова", "9")
student.add_grade(5)
student.add_grade(6)
student.add_grade(8)
# Выводим информацию о студенте
student.show_info()
