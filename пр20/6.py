class PositiveDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Value must be positive")
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name

class MyClass:
    attr = PositiveDescriptor()

obj = MyClass()
obj.attr = 42
print(obj.attr)