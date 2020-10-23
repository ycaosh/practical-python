# pcost.py
#
# Exercise 1.27
import csv


def portfolio_cost(filename):
    cost = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                cost += int(row[1]) * float(row[2])
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return cost


cost = portfolio_cost('data/portfolio.csv')
print(f'Total cost {cost:.2f}')
