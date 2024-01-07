N, M = map(int, input().split())
S = [input() for _ in range(N)]

# print(S)

count = 0

for i in range(N):
    for ii in range(i+1, N):
        for j in range(M):
            if S[i][j] == "x" and S[ii][j] =="x":
                break
            if j == M-1:
                count += 1

print(count)
