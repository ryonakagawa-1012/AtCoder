N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
B = A.copy()

for i in range(Q-P+1):
    B[R-1+i] = A[P-1+i]
    B[P-1+i] = A[R-1+i]

print(" ".join(str(b) for b in B))
