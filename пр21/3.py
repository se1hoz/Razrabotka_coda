class WithSlots:
    __slots__ = ('attr',)
    pass

class WithoutSlots:
    pass

obj1 = WithSlots()
obj2 = WithoutSlots()

obj1.attr = 1
obj2.attr = 1
obj2.new_attr = 2

try:
    obj1.new_attr = 2
except AttributeError as e:
    print(f"С объектом WithSlots: {e}")

print("Объект WithoutSlots может добавлять новые атрибуты")
print("Объект WithSlots не может добавлять новые атрибуты")