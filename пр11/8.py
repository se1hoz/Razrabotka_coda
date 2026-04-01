def check_positive(func):
    def wrapper(*args, **kwargs):
        if any(arg < 0 for arg in args):
            print("Error")
            return
        return func(*args, **kwargs)
    return wrapper

# Пример 1
@check_positive
def multiply(a, b):
    print(a * b)

multiply(3, 4)
multiply(3, -1)
