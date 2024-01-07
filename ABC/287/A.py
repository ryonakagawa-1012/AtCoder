N = int(input())
S = [input() for _ in range(N)]

count = 0

for _ in S:
    if _ == "For":
        count += 1

if count > len(S)//2:
    print("Yes")
else:
    print("No")
