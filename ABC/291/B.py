import numpy as np

N = int(input())
X = list(map(int, input().split()))

X.sort()

for i in range(N):
    X.pop(0)
    X.pop(-1)

print(np.mean(X))
