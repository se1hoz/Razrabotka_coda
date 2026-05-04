class LoggingGetDescriptor:
    def __get__(self, instance, owner):
        print('Getting value')
        return self.value
    def __set__(self, instance, value):
        self.value = value

class MyClass:
    attr = LoggingGetDescriptor()

obj = MyClass()
obj.attr = 42
print(obj.attr)