n, x = map(int, input().split())
strings = []
for i in range(26):
    for _ in range(n):
        strings.append(chr(ord("A")+i))
print(strings[x-1])
