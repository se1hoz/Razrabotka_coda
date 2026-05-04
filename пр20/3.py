class LoggingSetDescriptor:
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        print('Setting value')
        self.value = value

class MyClass:
    attr = LoggingSetDescriptor()

obj = MyClass()
obj.attr = 42
print(obj.attr)