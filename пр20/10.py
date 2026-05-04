class LengthLimitDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Value must be string")
        if len(value) > 10:
            raise ValueError("String length must be <= 10")
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name

class MyClass:
    attr = LengthLimitDescriptor()

obj = MyClass()
obj.attr = "hello"
print(obj.attr)