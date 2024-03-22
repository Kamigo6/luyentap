n = int(input())
if n < 0:
    print('NO')
else:
    print('YES' if n**0.5 % 1 == 0 else 'NO')
