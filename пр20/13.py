class RoundDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        instance.__dict__[self.name] = round(value, 2)
    def __set_name__(self, owner, name):
        self.name = name

class MyClass:
    number = RoundDescriptor()

obj = MyClass()
obj.number = 3.14159
print(obj.number)