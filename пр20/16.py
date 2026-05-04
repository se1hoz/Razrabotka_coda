class LinkedDescriptor:
    def __init__(self, other_field):
        self.other_field = other_field
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
        setattr(instance, self.other_field, value * 2)
    def __set_name__(self, owner, name):
        self.name = name

class MyClass:
    a = LinkedDescriptor('b')
    def __init__(self):
        self.b = 0

obj = MyClass()
obj.a = 5
print(obj.a)
print(obj.b)