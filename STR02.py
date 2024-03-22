def uniform(s):
    s = s.strip()
    s = s.lower()
    while s.find("  ") > 0:
        s = s.replace('  ', " ")
    s = s.title()
    print(s)


if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        s = input()
        uniform(s)
