input()
arr = [int(x) for x in input().split()]
m = max(arr)

while m == max(arr):
    arr.remove(m)
    if len(arr) == 0:
        break

if len(arr) < 1:
    print("NOT FOUND")
else:
    print(max(arr))
