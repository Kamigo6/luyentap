from math import factorial

n, k = [int(x) for x in input().split()]
c = factorial(n)/(factorial(k) * factorial(n - k))
print(int(c))
