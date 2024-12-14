"""
1) Разработайте класс BankAccount, который имеет атрибуты balance (баланс) и owner (владелец).
Реализуйте методы deposit(amount) для внесения средств на счет и withdraw(amount) для снятия средств со счета.
Учтите возможность проверки наличия достаточного баланса перед снятием.
"""
class BankAccount:
    def __init__(self, balance: int, owner: str):
        self.balance = balance
        self.owner = owner


    def deposit(self, amount: int) -> None:
        """
        Increment balance of current account by amount.

        :param amount: quantity of money for deposit.
        """
        self.balance += amount


    def withdraw(self, amount: int) -> None:
        """
        Increment balance of current account by amount.

        :param amount: quantity of money for withdraw.
        """
        if self.balance < amount:
            print('Not enough money for withdraw.')
        else:
            self.balance -= amount