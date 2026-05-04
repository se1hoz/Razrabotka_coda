class ComplexDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be number")
        if value < 0 or value > 100:
            raise ValueError("Value must be between 0 and 100")
        old = instance.__dict__.get(self.name, None)
        print(f"Setting value: {value}")
        if old is not None:
            print(f"Previous value was: {old}")
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        raise AttributeError("Cannot delete attribute")
    def __set_name__(self, owner, name):
        self.name = name

class MyClass:
    attr = ComplexDescriptor()

obj = MyClass()
obj.attr = 50
print(obj.attr)