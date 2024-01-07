H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = [["" for _ in range(W)] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if A[i][j] == 0:
            ans[i][j] = "."
        else:
            ans[i][j] = chr(ord("A") + A[i][j] - 1)

for _ in ans:
    print("".join(_))
