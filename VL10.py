n = input()

cnt = 0
for i in range(0, len(n)):
    if n[i].isnumeric():
        cnt += 1

print(cnt)
