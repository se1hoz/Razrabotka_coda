class Student:
    __slots__ = ('name', 'age', 'grades')
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self, value):
        self.grades.append(value)
    
    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

s1 = Student("Alice", 20)
s1.add_grade(5)
s1.add_grade(4)
s1.add_grade(5)

s2 = Student("Bob", 22)
s2.add_grade(3)
s2.add_grade(4)

try:
    s1.new_attr = "test"
except AttributeError as e:
    print(f"Нельзя добавить новый атрибут: {e}")

print(f"{s1.name}, средний балл: {s1.average():.2f}")
print(f"{s2.name}, средний балл: {s2.average():.2f}")