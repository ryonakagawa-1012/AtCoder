import copy

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

A_rotate = [[0]*N for _ in range(N)]

for k in range(4):
    Cond_Flag = True
    for i in range(N):
        for j in range(N):
            A_rotate[j][N-1-i] = A[i][j]

    for i in range(N):
        for j in range(N):
            if A_rotate[i][j] == 1 and B[i][j] != 1:
                Cond_Flag = False

    if Cond_Flag:
        print("Yes")
        exit()

    A = copy.deepcopy(A_rotate)

print("No")
