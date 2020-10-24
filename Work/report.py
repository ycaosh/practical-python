# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                record['shares'] = int(record['shares'])
                record['price'] = float(record['price'])
                portfolio.append(record)
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
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


def make_report(portfolio, prices):
    report = []
    for r in portfolio:
        report.append((r['name'], r['shares'], prices[r['name']],
                       prices[r['name']]-r['price']))
    return report


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')
name, shares, price, change = headers
print(f'{name:>10s} {shares:>10s} {price:>10s} {change:>10s}')
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d}',
          f'${price:>.2f}'.rjust(10), f'{change:>10.2f}')
