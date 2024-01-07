n, x = map(int, input().split())
s = list(map(int, input().split()))
print(sum(_ for _ in s if _ <= x))
