H, W = map(int, input().split())
S = list(input() for _ in range(H))

count = 0

for s in S:
    for esu in s:
        if esu == "#":
            count += 1

print(count)
