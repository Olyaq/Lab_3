import math

class Shape:
    def area(self):
        return 0
    
    def perimeter(self):
        return 0
    
    def __str__(self):
        return "Фигура"

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def area(self):
        return self.w * self.h
    
    def perimeter(self):
        return 2 * (self.w + self.h)
    
    def __str__(self):
        return f"Прямоугольник {self.w}x{self.h}"

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return math.pi * self.r ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.r
    
    def __str__(self):
        return f"Круг радиусом {self.r}"

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    
    def __str__(self):
        return f"Треугольник со сторонами {self.a}, {self.b}, {self.c}"

def show_shape_info(shape):
    print(f"{shape}")
    print(f"Площадь: {shape.area():.1f}")
    print(f"Периметр: {shape.perimeter():.1f}\n")

# Пример использования
if __name__ == "__main__":
    figures = [
        Rectangle(2, 4),
        Circle(2),
        Triangle(5, 3, 5)
    ]
    
    for figure in figures:
        show_shape_info(figure)
