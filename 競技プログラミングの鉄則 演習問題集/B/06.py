N = int(input())
A = list(map(int, input().split()))
Q = int(input())
LR = [list(map(int, input().split())) for _ in range(Q)]
L = [_[0] for _ in LR]
R = [_[1] for _ in LR]

Atari_sum = [0] * (N+1)
Hazure_sum = [0]*(N+1)

for i in range(1, N+1):
    Atari_sum[i] += Atari_sum[i - 1]
    Hazure_sum[i] += Hazure_sum[i-1]
    if A[i-1] == 1:
        Atari_sum[i] += 1
    else:
        Hazure_sum[i] += 1

# print(Atari_sum)
# print(Hazure_sum)

for i in range(Q):
    if Atari_sum[R[i]] - Atari_sum[L[i]-1] > Hazure_sum[R[i]] - Hazure_sum[L[i] - 1]:
        print("win")
    elif Atari_sum[R[i]] - Atari_sum[L[i]-1] < Hazure_sum[R[i]] - Hazure_sum[L[i] - 1]:
        print("lose")
    else:
        print("draw")
