from collections import defaultdict

n, m, t = map(int, input().split())
a = list(map(int, input().split()))
xy = defaultdict(int)
for _ in range(m):
    x, y = map(int, input().split())
    xy[x] = y

for i in range(1, n):
    t -= a[i-1] - xy[i]
    if t <= 0:
        print("No")
        exit()

print("Yes")
