class BankAccount:
    overdraft_fee = 20
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance < 0:
            self.balance = self.balance - 20

college_checking = BankAccount(1000)
college_checking.withdraw(200)
college_checking.withdraw(500)
college_checking.deposit(100)
college_checking.withdraw(600)
print(college_checking.balance)

class OverdraftProtectionAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance < 0:
            print("There's insufficient funds in your account to complete this transaction")
            self.balance = self.balance + amount

personal_checking = OverdraftProtectionAccount(100)
personal_checking.withdraw(20)
personal_checking.withdraw(50)
personal_checking.deposit(12)
personal_checking.withdraw(60)
print(personal_checking.balance)