class Rectangle:
    __slots__ = ('width', 'height')
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

r = Rectangle(5, 10)
print(f"Площадь прямоугольника: {r.area()}")