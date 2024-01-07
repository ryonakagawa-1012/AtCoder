N = int(input())
ans = []
for i in range(9, -1, -1):
    ans.append((N//(2**i)) % 2)
print("".join(str(_) for _ in ans))
