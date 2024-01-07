N = int(input())

C = [0]*N

A = [[]*N]*N

for i in range(N):
    C[i] = int(input())
    A[i] = list(map(int, input().split()))

X = int(input())
# ここまで

find_X = []

for i in range(N):
    if X in A[i]:
        find_X.append(len(A[i]))
    else:
        find_X.append(None)

find_min = 37

for i in range(N):
    if find_X[i] is not None:
        find_min = min(find_min, find_X[i])

# print(find_X)
#
# print(find_min)

ans = []

for i in range(N):
    if find_X[i] == find_min:
        ans.append(i+1)

print(len(ans))

ans = [str(a) for a in ans]
ans = " ".join(ans)

print(ans)
