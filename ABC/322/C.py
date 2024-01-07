import bisect

N, M = map(int, input().split())

A = list(map(int, input().split()))

# # print(bool(1 == a for a in A if a == 1))
# print(bisect.bisect_left(A, 1))

for i in range(1, N+1):
    if i == A[bisect.bisect_left(A, i)]:
        print(0)
    else:
        print(A[bisect.bisect_left(A, i)]-i)
        # print(min(a for a in A if a > i)-i)
