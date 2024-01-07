N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Sum = 0

for i in range(M):
    Sum += A[B[i]-1]

print(Sum)
