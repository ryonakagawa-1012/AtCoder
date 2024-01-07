n = int(input())
ans = []
for i in range(n):
    tmp = []
    for j in range(i+1):
        if j == 0 or j == i:
            tmp.append(1)
        else:
            tmp.append(ans[i-1][j-1]+ans[i-1][j])
    ans.append(tmp)

for ANS in ans:
    print(*ANS, sep=" ")
