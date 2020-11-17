from typedproperty import String, Integer, Float


class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    # @property
    # def shares(self):
    #     return self._shares

    # @shares.setter
    # def shares(self, value):
    #     if not isinstance(value, int):
    #         raise TypeError('expected an integer')
    #     self._shares = value

    def cost(self):
        return self.shares * self.price

    def sell(self, n):
        if self.shares - n >= 0:
            self.shares -= n
        return self.shares

    def __repr__(self):
        return f'Stock(\'{self.name}\', {self.shares}, {self.price})'
