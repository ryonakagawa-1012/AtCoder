S = input()

S_size = len(S)

ans = 0

for i in range(S_size+1):
    for j in range(i, S_size+1):
        if S[i:j] == S[i:j][::-1]:
            ans = max(ans, j-i)

print(ans)
