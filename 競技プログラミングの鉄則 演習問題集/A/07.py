D = int(input())
N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]
L = [_[0] for _ in LR]
R = [_[1] for _ in LR]

ratio = [0] * (D + 2)

for i in range(N):
    ratio[L[i]] += 1
    ratio[R[i] + 1] -= 1

ans = [0]*(D+1)

for i in range(1, D+1):
    ans[i] = ans[i-1] + ratio[i]
    print(ans[i])
