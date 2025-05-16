# Загружаем модуль math для математических операций 
import math

# Базовый класс Shape с методами
class Shape:
    # Метод для вычисления площади 
    def area(self):
        return 0
    
    # Метод для вычисления периметра
    def perimeter(self):
        return 0
    
    # Метод для строкового представления объекта
    def __str__(self):
        return "Фигура"

# Класс Rectangle (Прямоугольник), идет от Shape
class Rectangle(Shape):
    # Конструктор класса, принимает ширину (w) и высоту (h)
    def __init__(self, w, h):
        self.w = w  # Сохраняем ширину
        self.h = h  # Сохраняем высоту
    
    # Переопределяем метод area для прямоугольника (площадь = ширина * высота)
    def area(self):
        return self.w * self.h
    
    # Переопределяем метод perimeter (периметр = 2*(ширина + высота))
    def perimeter(self):
        return 2 * (self.w + self.h)
    
    # Переопределяем строковое представление
    def __str__(self):
        return f"Прямоугольник {self.w}x{self.h}"

# Класс Circle (Круг), идет от Shape
class Circle(Shape):
    # Конструктор, принимает радиус (r)
    def __init__(self, r):
        self.r = r  # Сохраняем радиус
    
    # Переопределяем метод area (площадь круга = pr²)
    def area(self):
        return math.pi * self.r ** 2
    
    # Переопределяем метод perimeter (длина окружности = 2pr)
    def perimeter(self):
        return 2 * math.pi * self.r
    
    # Переопределяем строковое представление
    def __str__(self):
        return f"Круг радиусом {self.r}"

# Класс Triangle (Треугольник), идет от Shape
class Triangle(Shape):
    # Конструктор, принимает три стороны 
    def __init__(self, a, b, c):
        self.a = a  # 1 сторона
        self.b = b  # 2 сторона
        self.c = c  # 3 сторона
    
    # Переопределяем метод perimeter (периметр = сумма сторон)
    def perimeter(self):
        return self.a + self.b + self.c
    
    # Переопределяем метод area (по формуле Герона)
    def area(self):
        p = self.perimeter() / 2  # Полупериметр
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    # Переопределяем строковое представление
    def __str__(self):
        return f"Треугольник со сторонами {self.a}, {self.b}, {self.c}"

# Функция для вывода информации о фигуре
def show_shape_info(shape):
    print(f"{shape}")  # Выводим строковое представление фигуры
    print(f"Площадь: {shape.area():.1f}")  # Выводим площадь с 1 знаком после запятой
    print(f"Периметр: {shape.perimeter():.1f}\n")  # Выводим периметр с 1 знаком после запятой

# Основной блок выполнения (выполняется только при прямом запуске файла)
if __name__ == "__main__":
    # Создаем список фигур
    figures = [
        Rectangle(2, 4),  # Прямоугольник 2x4
        Circle(2),        # Круг радиусом 2
        Triangle(5, 3, 5) # Треугольник со сторонами 5, 3, 5
    ]
    
    # Для каждой фигуры в списке выводим информацию
    for figure in figures:
        show_shape_info(figure)
