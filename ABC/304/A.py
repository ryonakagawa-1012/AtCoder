N = int(input())

SA = list(input().split() for _ in range(N))

S = [_[0] for _ in SA]
A = [int(_[1]) for _ in SA]

ans = []*5

for i in range(A.index(min(A)), N):
    ans.append(S[i])

for i in range(0, A.index(min(A))):
    ans.append(S[i])

print(" ".join(ans))
