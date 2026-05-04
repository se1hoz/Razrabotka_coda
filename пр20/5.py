class IntDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Value must be int")
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name

class MyClass:
    attr = IntDescriptor()

obj = MyClass()
obj.attr = 42
print(obj.attr)