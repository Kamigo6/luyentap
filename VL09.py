from math import factorial

arg = input().split()

x = float(arg[0])
n = int(arg[1])

sum = 0
for i in range(1, n + 1):
    sum += x**i/factorial(i)

print(f'{sum:.2f}')
