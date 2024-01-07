N = int(input())

A = list(map(int, input().split()))

SUM = []

for i in range(1, N+1):
    SUM.append(sum(A[7*i-7:7*i]))

print(" ".join(map(str, SUM)))
