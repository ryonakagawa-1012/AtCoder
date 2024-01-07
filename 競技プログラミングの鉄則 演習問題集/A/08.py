from itertools import accumulate
from pprint import pprint

H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
ABCD = [list(map(int, input().split())) for _ in range(Q)]
# print(X)

X.insert(0, [0]*W)

for i in range(H+1):
    X[i] = list(accumulate(X[i], initial=0))
# print(X)
for i in range(W+1):
    for j in range(1, H+1):
        X[j][i] = X[j-1][i] + X[j][i]
# print(X)

# pprint(X)

for abcd in ABCD:
    a, b, c, d = abcd[0], abcd[1], abcd[2], abcd[3]
    print(X[c][d]+X[a-1][b-1]-X[c][b-1]-X[a-1][d])
