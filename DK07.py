def eq1(a, b):
    if a == 0:
        if b == 0:
            print("WOW")
        else:
            print("NO")
    else:
        print(f'{((-b)/a):.2f}')


def eq2(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("NO")
    else:
        sol1 = (-b - delta**0.5)/(2*a)
        sol2 = (-b + delta**0.5)/(2*a)
        if delta != 0:
            print(f'{sol1:.2f}', f'{sol2:.2f}')
        else:
            print(f'{sol1:.2f}')


a, b, c = [int(x) for x in input().split()]
if a == 0:
    eq1(b, c)
else:
    eq2(a, b, c)
