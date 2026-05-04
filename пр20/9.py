class CounterDescriptor:
    def __init__(self):
        self.counter = 0
    def __get__(self, instance, owner):
        self.counter += 1
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name

class MyClass:
    attr = CounterDescriptor()

obj = MyClass()
obj.attr = 42
print(obj.attr)
print(obj.attr)
print(obj.attr)
print(f"Access count: {MyClass.attr.counter}")