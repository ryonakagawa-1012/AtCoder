from itertools import accumulate

N = int(input())
BOX = [[0]*1502 for _ in range(1502)]
for _ in range(N):
    A, B, C, D = map(int, input().split())
    # print(A, B, C, D)
    BOX[A][B] += 1
    BOX[C][D] += 1
    BOX[A][D] -= 1
    BOX[C][B] -= 1

for i in range(0, 1501):
    for j in range(1, 1501):
        BOX[i][j] = BOX[i][j-1] + BOX[i][j]
for i in range(1, 1501):
    for j in range(0, 1501):
        BOX[i][j] = BOX[i-1][j] + BOX[i][j]

Answer = 0
for box in BOX:
    for i in range(1502):
        if box[i] >= 1:
            Answer += 1

print(Answer)
