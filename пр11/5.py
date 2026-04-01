def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Пример 1
@logger
def say_hello():
    print("Hello!")

say_hello()
