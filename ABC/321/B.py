Round = list(map(int, input().split()))

A = list(map(int, input().split()))

N = Round[0]
X = Round[1]

S = []

Result = 0

for i in range(0, 101):
    # print(i)
    A.append(i)
    S = sorted(A)
    # print(S)

    for j in range(1, N-1):
        Result += S[j]

    # print(Result)

    if Result >= X:
        print(i)
        exit()

    A.remove(i)
    Result = 0

print(-1)
