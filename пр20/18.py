class NumberListDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise TypeError("Value must be list")
        for item in value:
            if not isinstance(item, (int, float)):
                raise TypeError("All items must be numbers")
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name

class MyClass:
    numbers = NumberListDescriptor()

obj = MyClass()
obj.numbers = [1, 2, 3, 4, 5]
print(obj.numbers)