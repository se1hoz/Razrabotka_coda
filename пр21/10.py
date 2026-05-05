class Employee:
    __slots__ = ('name', 'salary')
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def increase_salary(self, percent):
        self.salary += self.salary * percent / 100
        print(f"Новая зарплата {self.name}: {self.salary}")

e = Employee("Petr", 50000)
e.increase_salary(10)