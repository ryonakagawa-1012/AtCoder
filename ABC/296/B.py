S = [input() for _ in range(8)]

wid = [chr(_) for _ in range(ord("a"), ord("i"))]
length = [str(_) for _ in range(1, 9)]

# print(S)
# print(wid)
# print(length)

for y in range(8):
    for x in range(8):
        if S[y][x] == "*":
            # print(x, y)
            print(wid[x]+length[7-y])
