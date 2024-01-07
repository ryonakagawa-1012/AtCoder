from itertools import accumulate
from pprint import pprint

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
abcd = [list(map(int, input().split())) for _ in range(Q)]

X_max = max(x[0] for x in XY)
Y_max = max(y[1] for y in XY)

BOX = [[0] * (X_max + 1) for _ in range(Y_max + 1)]

for xy in XY:
    x, y = xy[0], xy[1]
    BOX[y][x] += 1

# pprint(BOX)
# print()

for i in range(Y_max+1):
    BOX[i] = list(accumulate(BOX[i]))

# pprint(BOX)
# print()

for i in range(X_max+1):
    for j in range(1, Y_max+1):
        BOX[j][i] = BOX[j-1][i] + BOX[j][i]

# pprint(BOX)
# print()

for ABCD in abcd:
    a, b, c, d = ABCD[0], ABCD[1], ABCD[2], ABCD[3]
    # print(ABCD)
    print(BOX[d][c] + BOX[b-1][a-1] - BOX[d][a-1] - BOX[b-1][c])
