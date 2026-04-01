class Calculator:
    def calculate(self, x, y=None):
        if y is None:
            return x ** 2
        return x + y

class AdvancedCalculator(Calculator):
    def calculate(self, x, y=None):
        return super().calculate(x, y) + 10

def log_call(func):
    def wrapper(*args, **kwargs):
        print("Function called")
        return func(*args, **kwargs)
    return wrapper

# Пример 1
calc = AdvancedCalculator()
calc.calculate = log_call(calc.calculate)
print(calc.calculate(5))
print(calc.calculate(2, 3))
