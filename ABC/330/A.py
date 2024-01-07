n, l = map(int, input())
a = list(map(int, input().split()))
ans = 0
for A in a:
    if A >= l:
        ans += 1
print(ans)
