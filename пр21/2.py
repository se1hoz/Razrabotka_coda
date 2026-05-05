class Animal:
    __slots__ = ('type', 'weight')

a = Animal()
a.type = "Dog"
a.weight = 10

try:
    a.color = "brown"
except AttributeError as e:
    print(f"Ошибка: {e}")
print("Нельзя добавить новый атрибут color, так как __slots__ ограничивает атрибуты")