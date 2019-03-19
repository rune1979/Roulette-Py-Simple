


class wallet:
    def __init__(self, amount):
        self.amount = amount

    def withdraw_amount(self, withdraw):
        self.amount = self.amount - withdraw
        print("New account balance: ", self.amount)

    def add_amount(self, toadd):
        self.amount = self.amount + toadd
    def print_amount(self):
        return self.amount


