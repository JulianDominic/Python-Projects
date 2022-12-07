class Bank_Account:
    def __init__(self, name, opening_balance):
        self.name = name
        self.balance = opening_balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def check_balance(self):
        if self.balance >= 0:
            print(f"You current balance is ${self.balance:.2f}.")
        else:
            print(f"Your bank account has been overdrawn. You current balance is -${-self.balance:.2f}.")

# create Bank_Account object
account_001 = Bank_Account("James", 100)

# deposit
account_001.deposit(20)
account_001.check_balance()

# withdraw
account_001.withdraw(50)
account_001.check_balance()


# overdrawn status
account_001.withdraw(80)
account_001.check_balance()