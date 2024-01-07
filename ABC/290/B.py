N, K = map(int, input().split())
S = list(input())

T = []
count = 0

for i in range(N):
    if S[i] == "o" and count < K:
        T.append("o")
        count += 1
    else:
        T.append("x")

print("".join(T))
