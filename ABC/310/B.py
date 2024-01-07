N, M = map(int, input().split())
PCF = list(list(map(int, input().split())) for _ in range(N))

PCF.sort(key=lambda x: x[0])

P = [_[0] for _ in PCF]
C = [_[1] for _ in PCF]
F = [_[2:] for _ in PCF]
# print(P)
# print(C)
# print(F)
# print()

flag = False

for j in range(N):
    for i in range(1, N):
        # print(i, j)
        # print(P[j] <= P[i])
        # print(set(F[j]) >= set(F[i]))
        # print((P[j] < P[i] or C[j] > C[i]))
        # print()
        if P[j] <= P[i] and set(F[j]) >= set(F[i]) and (P[j] < P[i] or C[j] > C[i]):
            # print(i, j)
            # print()
            flag = True

if flag:
    print("Yes")
else:
    print("No")
