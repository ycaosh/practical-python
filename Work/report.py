# report.py
#
# Exercise 2.4
import csv
import fileparse


def read_portfolio(filename):
    portfolio = fileparse.parse_csv(
        filename, select=['name', 'shares', 'price'], types=[str, int, float])
    return portfolio


def read_prices(filename):
    prices = fileparse.parse_csv(
        filename, types=[str, float], has_headers=False)
    return dict(prices)


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


def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    name, shares, price, change = headers
    print(f'{name:>10s} {shares:>10s} {price:>10s} {change:>10s}')
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d}',
              f'${price:>.2f}'.rjust(10), f'{change:>10.2f}')


def portfolio_report(portfoliofile, pricefile):
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)
    report = make_report(portfolio, prices)
    print_report(report)


def main(argv):
    portfolio_report(argv[1], argv[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)
