class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} added to the account. Current balance: {self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds in the account.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn from the account. Remaining balance: {self.balance}")

    def __str__(self):
        return f"Account Owner: {self.owner}\nBalance: {self.balance}"


if __name__ == "__main__":
    acc = Account("Ali", 5000)
    print(acc)
    acc.deposit(2000)
    acc.withdraw(3000)
    acc.withdraw(5000)
    acc.deposit(-500)