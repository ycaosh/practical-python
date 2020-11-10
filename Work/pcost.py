# pcost.py
#
# Exercise 1.27
import csv
import report


def portfolio_cost(filename):
    cost = 0
    portfolio = report.read_portfolio(filename)
    for d in portfolio:
        cost += d.cost()
    return cost


def main(argv):
    cost = portfolio_cost(argv[1])
    print(f'Total cost {cost:.2f}')


if __name__ == '__main__':
    import sys
    main(sys.argv)
