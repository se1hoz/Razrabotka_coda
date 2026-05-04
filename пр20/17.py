class CachedDescriptor:
    def __init__(self, func):
        self.func = func
        self.cached = None
    def __get__(self, instance, owner):
        if self.cached is None:
            self.cached = self.func(instance)
        return self.cached

class MyClass:
    def __init__(self, x):
        self.x = x
    @CachedDescriptor
    def heavy(self):
        print("Computing...")
        return self.x * 100

obj = MyClass(5)
print(obj.heavy)
print(obj.heavy)