from itertools import accumulate
from pprint import pprint

H, W, N = map(int, input().split())
BOX = [[0]*(W+2) for _ in range(H+2)]
for _ in range(N):
    A, B, C, D = map(int, input().split())
    BOX[A][B] += 1
    BOX[C+1][D+1] += 1
    BOX[A][D+1] -= 1
    BOX[C+1][B] -= 1

# pprint(BOX)
# print()

for i in range(H+1):
    BOX[i] = list(accumulate(BOX[i]))

# pprint(BOX)
# print()

for i in range(1, W+1):
    for j in range(1, H+1):
        BOX[j][i] += BOX[j-1][i]

# pprint(BOX)

for i in range(1, H+1):
    print(" ".join(str(BOX[i][_]) for _ in range(1, W+1)))
