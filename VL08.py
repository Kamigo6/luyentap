a, b = [int(x) for x in input().split()]
a = a - a % 2
b = b - b % 2
sum = (b - a + 2)*(b + a)/4
print(int(sum))
