N, D = map(int, input().split())

S = [input() for _ in range(N)]

Hima_Day = [False]*D
Hima_count = [0]*D

# print([s[1] for s in S])
# print(["o"]*N)

for i in range(D):
    if [s[i] for s in S] == ["o"]*N:
        Hima_Day[i] = True

# print(Hima_Day)

for i in range(D):
    if Hima_Day[i]:
        for j in range(i, D):
            if Hima_Day[j]:
                Hima_count[i] += 1
            else:
                break

print(max(Hima_count))
