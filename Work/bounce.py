# bounce.py
#
# Exercise 1.5
height = 100
n = 1
back = 3 / 5
while n < 11:
    print(n, round(height*back, 4))
    n += 1
    height *= back
