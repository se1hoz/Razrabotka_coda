class OnceDescriptor:
    def __init__(self):
        self.set = False
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if self.set:
            raise AttributeError("Cannot change value after first assignment")
        instance.__dict__[self.name] = value
        self.set = True
    def __set_name__(self, owner, name):
        self.name = name

class MyClass:
    const = OnceDescriptor()

obj = MyClass()
obj.const = 42
print(obj.const)