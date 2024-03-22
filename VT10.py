input()
arr = [int(x) for x in input().split()]
arr.sort(reverse=True)
print(*arr)
