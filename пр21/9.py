import math

class Circle:
    __slots__ = ('radius',)
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

c = Circle(5)
print(f"Площадь круга: {c.area():.2f}")