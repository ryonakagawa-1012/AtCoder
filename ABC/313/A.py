N = int(input())

P = list(map(int, input().split()))

Max = 0

for i in range(1,N):
    Max = max(Max, P[i])

if Max+1-P[0] < 0:
    print(0)
else:
    print(Max+1-P[0])
