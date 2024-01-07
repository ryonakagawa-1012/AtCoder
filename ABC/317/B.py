N = int(input())

A = list(map(int, input().split()))

A.sort()

ans = 0

for i in range(N-1):
    if A[i]+1 != A[i+1]:
        ans = A[i] + 1

print(ans)
