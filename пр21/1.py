class Person:
    __slots__ = ('name', 'age')

p = Person()
p.name = "Alice"
p.age = 25
print(p.name, p.age)