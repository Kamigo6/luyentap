n = int(input())
arr = [int(x) for x in input().split()]

first = arr[0]
last = arr[n-1]
arr.remove(first)
arr.pop()
arr.sort()
arr.append(last)
arr.insert(0, first)
print(*arr)