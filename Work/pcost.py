# pcost.py
#
# Exercise 1.27
import csv
import report


def portfolio_cost(filename):
    cost = 0
    portfolio = report.read_portfolio(filename)
    for d in portfolio:
        cost += d['shares'] * d['price']
    return cost


cost = portfolio_cost('data/portfolio.csv')
print(f'Total cost {cost:.2f}')
