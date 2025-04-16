class Bank:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return(f'Amount of {amount} deposited, New balance is {self.balance}')
        else:
            return('Invalid deposit balance')
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            return(f'Amount of {amount} withdrawn, New balance is {self.balance}')
        else:
            return('Insufficient funds')

    def view_balance(self):
        return(f'Your balance is {self.balance}')

class SavingsAccount(Bank):
    def __init__(self,account_number, account_holder, balance,interest = 0.2):
        super().__init__(account_number,account_holder, balance)
        self.interest = interest

    def interest_applied(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest
            return(f'Interest of {self.interest} applied. Balance is {self.balance}')
        else:
            return('Insufficient funds')

John = SavingsAccount(20, 'John', 2000)
print(John.interest_applied())