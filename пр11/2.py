class Multiplier:
    def multiply(self, *args):
        if len(args) == 1:
            return args[0] ** 2
        elif len(args) == 2:
            return args[0] * args[1]

# Пример 1
m = Multiplier()
print(m.multiply(5))
print(m.multiply(2, 3))
