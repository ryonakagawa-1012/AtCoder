N = int(input())
S = list(map(int, input().split()))
A = []

for s in S:
    A.append(s-sum(A))

print(" ".join(str(a) for a in A))
