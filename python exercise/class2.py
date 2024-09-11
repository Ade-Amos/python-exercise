class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance is {self.balance}."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrew {amount}. New balance is {self.balance}."

# Create an instance and run the methods
account1 = BankAccount("Bob", 100)
print(account1.deposit(50))
print(account1.withdraw(30))