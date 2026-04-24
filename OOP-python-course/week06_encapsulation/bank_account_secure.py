class BankAccount_FGA:
    def __init__(self_FGA, balance_FGA):
        self_FGA.__balance_FGA = balance_FGA

    def deposit_FGA(self_FGA, amount_FGA):
        self_FGA.__balance_FGA += amount_FGA

    def withdraw_FGA(self_FGA, amount_FGA):
        if amount_FGA <= self_FGA.__balance_FGA:
            self_FGA.__balance_FGA -= amount_FGA
        else:
            print("Insufficient funds")

    def get_balance_FGA(self_FGA):
        return self_FGA.__balance_FGA

account_FGA = BankAccount_FGA(5000)
account_FGA.deposit_FGA(1000)
account_FGA.withdraw_FGA(2000)
print("Balance:", account_FGA.get_balance_FGA())

