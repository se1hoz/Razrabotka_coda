class EmailDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Value must be string")
        if '@' not in value:
            raise ValueError("Email must contain @")
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name

class User:
    email = EmailDescriptor()

u = User()
u.email = "test@example.com"
print(u.email)