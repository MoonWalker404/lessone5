# Класс `Банковский счет`
# Создайте класс `Банковский счет` с атрибутами для номера счета,
# имени владельца и текущего баланса. Реализуйте методы для снятия и
# добавления средств на счет, а также вывода текущего баланса.

class Accaunt():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успешно пополнили счет. Сумма на счете - {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print(f"Недостаточно средств на счете")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} рублей. Остаток на счете - {self.balance}")

    def all_balance(self):
        print(f"Текущий баланс - {self.balance}")

man = Accaunt("103337437", 7500000)

man.all_balance()
man.withdraw(150000)
man.withdraw(19500000)
man.deposit(12500000)