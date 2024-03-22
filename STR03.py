import string
alphabet = {key: 0 for key in string.ascii_lowercase}

s = input().lower()
s = s.replace(" ", '')
for i in range(0, len(s)):
    alphabet[s[i]] += 1
n = int(input())

for i in range(0, n):
    x = input()
    print(alphabet[x])
