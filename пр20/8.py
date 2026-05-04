class DefaultDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 'default')
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name

class MyClass:
    attr = DefaultDescriptor()

obj = MyClass()
print(obj.attr)
obj.attr = "set"
print(obj.attr)