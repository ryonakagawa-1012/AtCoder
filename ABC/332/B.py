k, g, m = map(int, input().split())
glass, mug = 0, 0
for _ in range(k):
    if glass == g:
        glass = 0
    elif mug == 0:
        mug = m
    else:
        while not (mug == 0 or glass == g):
            mug -= 1
            glass += 1
print(glass, mug)
