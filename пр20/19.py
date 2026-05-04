class CounterDescriptor:
    count = 0
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class CounterMeta(type):
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        CounterDescriptor.count += 1
        print(f"Objects created: {CounterDescriptor.count}")
        return instance

class MyClass(metaclass=CounterMeta):
    pass

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()