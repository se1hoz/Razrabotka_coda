class AgeDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Age must be int")
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name

class Person:
    age = AgeDescriptor()

p = Person()
p.age = 25
print(p.age)