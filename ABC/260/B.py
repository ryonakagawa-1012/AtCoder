n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A = {}
B = {}

for i in range(n):
    A[i+1] = a[i]
    B[i+1] = b[i]

# print(A)
A = dict(sorted(A.items(), key=lambda _: _[1], reverse=True)[x:])
# print(A)

tmp_B = {}
for i in A:
    tmp_B[i] = B[i]

# print(tmp_B)
B = dict(sorted(tmp_B.items(), key=lambda _: _[1], reverse=True)[y:])
# print(B)

AB = {}
for i in B:
    AB[i] = A[i]+ B[i]

# print(AB)
AB = dict(sorted(AB.items(), key=lambda _: _[1], reverse=True)[z:])
# print(AB)

ans = [i for i in range(1, n+1) if i not in AB]
print(*ans, sep="\n")
