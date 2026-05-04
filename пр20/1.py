class SimpleDescriptor:
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = value

class MyClass:
    attr = SimpleDescriptor()

obj = MyClass()
obj.attr = 42
print(obj.attr)