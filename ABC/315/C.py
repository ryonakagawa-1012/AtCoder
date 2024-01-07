N = int(input())
FS = list(list(map(int, input().split())) for _ in range(N))

FS.sort(reverse=True, key=lambda x: x[1])
F = [_[0] for _ in FS]
S = [_[1] for _ in FS]

# print(FS)
# print(F)
# print(S)

Manzoku = 0

if F[0] != F[1]:
    Manzoku = S[0] + S[1]
    for i in range(2, N):
        if F[0] == F[i]:
            Manzoku = max(Manzoku, S[0] + S[i]//2)
            break
else:
    Manzoku = S[0] + S[1] // 2
    for i in range(2, N):
        if F[0] != F[i]:
            Manzoku = max(Manzoku, S[0] + S[i])
            break

print(Manzoku)
