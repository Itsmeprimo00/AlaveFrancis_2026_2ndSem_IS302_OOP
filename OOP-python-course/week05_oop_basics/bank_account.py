class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name_FGA = account_name
        self.balance_FGA = balance

    def deposit(self, amount):
        self.balance_FGA += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if amount <= self.balance_FGA:
            self.balance_FGA -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Balance:", self.balance_FGA)


account = BankAccount("Juan", 5000)
account.deposit(1000)
account.withdraw(2000)
account.display_balance()


