import itertools

N, Q = map(int, input().split())
A = list(map(int, input().split()))
LR = [list(map(int, input().split())) for _ in range(Q)]
L = [_[0] for _ in LR]
R = [_[1] for _ in LR]

A_sum = list(itertools.accumulate(A, initial=0))

for i in range(Q):
    print(A_sum[R[i]] - A_sum[L[i] - 1])
