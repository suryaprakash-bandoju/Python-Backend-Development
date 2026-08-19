class BankAccount:
    def __init__(self, owner_name, account_number, balance=0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        return self.balance
    def get_balance(self):
        return self.balance
    def get_account_info(self):
        return f"Owner: {self.owner_name}. Account No: {self.account_number}. Balance: {self.balance}"


own1 = BankAccount("surya", 1234567890, 500)
own2 = BankAccount("prakash", 9876543210, 100)

print(own1.deposit(500))
print(own1.get_balance())
print(own1.withdraw(100))
print(own2.deposit(300))
print(own2.get_balance())
print(own2.withdraw(1000))

print(own1.get_account_info())
print(own2.get_account_info())
