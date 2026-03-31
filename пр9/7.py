from abc import ABC, abstractmethod


class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass


class BankAccount(Account):
    def __init__(self):
        self.__balance = 0  # Приватный атрибут

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


# Проверка [cite: 15]
account = BankAccount()
account.deposit(100)
print(account.get_balance())
