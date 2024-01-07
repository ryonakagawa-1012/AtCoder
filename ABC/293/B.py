N = int(input())
A = list(map(int, input().split()))
called = set()

for i in range(N):
    if i+1 not in called:
        called.add(A[i])

ans = set([_ for _ in range(1, N+1)]) - called

print(len(ans))
print(" ".join(str(_) for _ in ans))
