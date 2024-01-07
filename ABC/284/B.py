T = int(input())
N = []
A = []
for i in range(T):
    N.append(int(input()))
    A.append(list(map(int, input().split())))

# print(N)
# print(A)

ans = [0]*T

for i in range(T):
    for j in range(N[i]):
        if A[i][j] % 2 != 0:
            ans[i] += 1

for _ in ans:
    print(_)
