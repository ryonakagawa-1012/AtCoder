N, M = map(int, input().split())
C = input().split()
D = input().split()
P = list(map(int, input().split()))

SUM = 0

P_0 = P.pop(0)

DP = {d: p for d, p in zip(D, P)}


for i in range(N):
    SUM += DP.get(C[i], P_0)

print(SUM)
