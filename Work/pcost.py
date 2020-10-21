# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    cost = 0
    with open(filename, 'rt') as f:
        next(f)
        for line in f:
            row = line.strip().split(',')
            cost += int(row[1]) * float(row[2])
    return cost


cost = portfolio_cost('work/data/portfolio.csv')
print(f'Total cost {cost:.2f}')
