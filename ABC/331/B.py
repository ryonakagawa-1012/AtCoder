N, S, M, L = map(int, input().split())

ans = float("inf")

for s in range(101):
    for m in range(101):
        for l in range(101):
            if N <= 6*s+8*m+12*l:
                ans = min(ans, S*s+M*m+L*l)
print(ans)
