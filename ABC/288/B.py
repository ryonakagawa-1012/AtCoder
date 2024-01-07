N, K = map(int, input().split())
S = list(input().split() for _ in range(N))

del S[K:]

for _ in sorted(S):
    print("".join(_))
