from functools import reduce
def divisible(a): return a % 5 == 0


l = [12, 45, 10, 90, 69, 55]
m = print(list(filter(divisible, l)))
print(m)

from functools import reduce

def max(m, n):
    if m>n:
        return m
    return n

a = [1111,2,3,54,675,54,34]
maxNum = reduce(max, a)
print(maxNum)