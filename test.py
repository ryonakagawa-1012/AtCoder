from collections import defaultdict


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = []

normal = defaultdict(int)
answer = 0

loop = sum(A)

total = 0
for a in A:
    B.append(total)
    normal[total % M] += 1
    total += a

print(B)
print(normal)

for b in B:
    normal[b % M] -= 1
    answer += normal[b % M]
    normal[(b + loop) % M] += 1

print(answer)
