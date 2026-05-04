class LogChangeDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        old = instance.__dict__.get(self.name, None)
        if old is not None:
            print(f"Changing from {old} to {value}")
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name

class MyClass:
    attr = LogChangeDescriptor()

obj = MyClass()
obj.attr = 10
obj.attr = 20
print(obj.attr)