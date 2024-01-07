import copy

N = int(input())
A = [list(map(int, input())) for _ in range(N)]

ans = copy.deepcopy(A)

for i in range(N-1):
    ans[0][i+1] = A[0][i]
    ans[i+1][N-1] = A[i][N-1]
    ans[N-1][N-2-i] = A[N-1][N-1-i]
    ans[N-2-i][0] = A[N-1-i][0]

for _ in ans:
    print("".join(str(__)for __ in _))
