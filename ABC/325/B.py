N = int(input())
WX = list(list(map(int, input().split())) for _ in range(N))
# print(WX)
# WX.sort(reverse=True, key=lambda x: x[0])
W = [w[0] for w in WX]
X = [x[1] for x in WX]
# print(W)
# print(X)

count = [0 for _ in range(24)]

for i in range(24):
    for j in range(N):
        if i + X[j] >= 24:
            time = i + X[j] - 24
        else:
            time = i + X[j]
        # print(i, time)
        if 9 <= time <= 17:
            count[i] += W[j]
    # print("count:", count[i])

# print(count)

print(max(count))
