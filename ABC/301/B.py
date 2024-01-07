N = int(input())
A = list(map(int, input().split()))

Ans_A = []

for i in range(N):
    Ans_A.append(A[i])
    if i != N-1:
        if A[i] < A[i+1]:
            for j in range(1, A[i+1]-A[i]):
                Ans_A.append(A[i]+j)
        if A[i] > A[i+1]:
            for j in range(1, A[i]-A[i+1]):
                Ans_A.append(A[i]-j)

print(" ".join(str(ans) for ans in Ans_A))
