N = int(input())
S = [list(input()) for _ in range(N)]

Win = [0] * N

for i in range(N):
    for j in range(N):
        if S[i][j] == "o":
            Win[i] += 1

# print(Win)

Win_list = {}

for i in range(N):
    Win_list[i+1] = Win[i]

# print(Win_list)

Win_list = sorted(Win_list.items(), key=lambda win: win[1], reverse=True)

# print(Win_list)

ans, tmp = [_ for _ in zip(*Win_list)]

ans = [str(_) for _ in ans]

print(" ".join(ans))
