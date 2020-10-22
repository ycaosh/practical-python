# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            holding = {}
            holding['name'] = row[0]
            holding['shares'] = int(row[1])
            holding['price'] = float(row[2])
            portfolio.append(holding)
    return portfolio


def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) != 0:
                prices[row[0]] = float(row[1])
    return prices


def can_i_retire(portfolio_file, price_file):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(price_file)
    total_cost = 0.0
    total_value = 0.0
    for row in portfolio:
        total_cost += row['shares'] * row['price']
        total_value += row['shares'] * prices[row['name']]
    print('Total cost', total_cost)
    print('Current value', total_value)
    print('Gain', total_value - total_cost)
