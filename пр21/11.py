class Product:
    __slots__ = ('name', 'price')
    
    def __init__(self, name, price):
        self.name = name
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.price = price

try:
    p1 = Product("Phone", 1000)
    print(p1.name, p1.price)
    p2 = Product("Bad", -50)
except ValueError as e:
    print(f"Ошибка: {e}")