x, y, n = map(int, input().split())

ans = float("inf")

for i in range(100):
    for iii in range(34):
        if i + 3*iii == n:
            ans = min(ans, i*x + y*iii)

print(ans)
