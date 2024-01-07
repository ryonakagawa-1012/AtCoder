import numpy as np
import math

N, M = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(M)]

pair = [[]*2]*(N-1)*M

k = 0

for i in range(M):
    for j in range(N-1):
        # print(i)
        pair[k] = a[i][j:j+2]
        k += 1
        # print(pair)

# print(pair)
pair = np.sort(pair)
# print(pair)
pair = set(list(map(tuple, pair)))
# print(pair)

# print(len(pair))
# print(math.comb(N, 2))

print(math.comb(N, 2) - len(pair))
