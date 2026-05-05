class BankAccount:
    __slots__ = ('balance',)
    
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Пополнено: {amount}, Баланс: {self.balance}")
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Снято: {amount}, Баланс: {self.balance}")
        else:
            print("Недостаточно средств")

acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)