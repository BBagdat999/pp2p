class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, d_cash):
        self.balance += d_cash
        print(f"{self.owner} успешно пополнил баланс на {d_cash}")
        print(f"На балансе имеется {self.balance}")

    def withdraw(self, w_cash):
        if self.balance < w_cash:
            print(f"{self.owner} запросил сумму больше текущего баланса")
        else:
            self.balance -= w_cash
            print(f"{self.owner} успешно снял с баланса {w_cash}")
            print(f"На балансе осталось {self.balance}")


kw = Account('Bagdat', 500)

kw.deposit(int(input('Введите сумму для пополнения: ')))
kw.withdraw(int(input('Введите сумму для снятия: ')))
kw.deposit(int(input('Введите сумму для пополнения: ')))
kw.withdraw(int(input('Введите сумму для снятия: ')))