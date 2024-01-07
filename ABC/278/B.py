def time_replace(h, m):
    A = h//10
    B = h-A*10
    C = m//10
    D = m-C*10
    B, C = C, B

    return A*10+B, C*10+D


def is_misjudge_time(h, m):
    return 0 <= h <= 23 and 0 <= m <= 59


def time_add(h, m):
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0

    return h, m


H, M = map(int, input().split())


while True:
    rep_H, rep_M = time_replace(H, M)
    if is_misjudge_time(rep_H, rep_M):
        print(H, M)
        exit()
    H, M = time_add(H, M+1)
