class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, n):
        if self.shares - n >= 0:
            self.shares -= n
        return self.shares

    def __repr__(self):
        return f'Stock(\'{self.name}\', {self.shares}, {self.price})'
