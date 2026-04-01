class Adder:
    def add(self, *args):
        if len(args) == 1:
            return args[0] + 10
        elif len(args) == 2:
            return args[0] + args[1]

# Пример 1
a = Adder()
print(a.add(5))
print(a.add(3, 4))
