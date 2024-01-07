Num = list(map(int, input().split()))

D = list(map(int, input().split()))

N = Num[0]
P = Num[1]
Q = Num[2]

print(min(P, Q + min(D)))
