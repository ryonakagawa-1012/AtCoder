N = int(input())

ABCD = [list(map(int, input().split())) for _ in range(N)]

A = [ABCD[i][0] for i in range(N)]
B = [ABCD[i][1] for i in range(N)]
C = [ABCD[i][2] for i in range(N)]
D = [ABCD[i][3] for i in range(N)]

# print(A)
# print(B)
# print(C)
# print(D)



BOX = [[False for i in range(100)] for j in range(100)]

# print(BOX)

for i in range(N):
    for y in range(C[i], D[i]):
        for x in range(A[i], B[i]):
            BOX[x][y] = True

# for y in range(100):
#     for x in range(100):
#         for i in range(N):
#             if A[i] <= x <= B[i] and C[i] <= y <= D[i]:
#                 BOX[x][y] = True

# print(BOX)

count = 0

for y in range(100):
    for x in range(100):
        if BOX[x][y]:
            count += 1

print(count)
