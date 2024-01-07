num = list(map(int, input().split()))
P = list(map(int, input().split()))

N = num[0]
H = num[1]
X = num[2]

for i in range(N):
    if H+P[i] >= X:
        print(i+1)
        break
