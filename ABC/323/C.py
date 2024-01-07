N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [list(input()) for _ in range(N)]

# print(A)
# print(S)

Score = [0]*N

for i in range(N):
    for j in range(M):
        if S[i][j] == "o":
            Score[i] += A[j]
    Score[i] += (i+1)

# print(Score)
Score_Max = max(Score)

ans = [0]*N

for i in range(N):
    Score_list = [(A[_], S[i][_]) for _ in range(M)]
    Score_list_sorted = sorted(Score_list, key=lambda score: score[0], reverse=True)
    A_sorted = [a[0] for a in Score_list_sorted]
    S_sorted = [s[1] for s in Score_list_sorted]
    # print(Score_list)
    # print(Score_list_sorted)
    # print(A_sorted)
    # print(S_sorted)
    if Score[i] < Score_Max:
        for j in range(M):
            if S_sorted[j] == "x":
                Score[i] += A_sorted[j]
                ans[i] += 1
            if Score_Max < Score[i]:
                break

for _ in ans:
    print(_)
