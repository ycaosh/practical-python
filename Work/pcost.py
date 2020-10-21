# pcost.py
#
# Exercise 1.27
cost = 0
with open(r'D:\cy\code\python\practical-python\Work\Data\portfolio.csv', 'rt') as f:
    next(f)
    for line in f:
        row = line.strip().split(',')
        cost += int(row[1]) * float(row[2])
print(f'Total cost {cost:.2f}')
