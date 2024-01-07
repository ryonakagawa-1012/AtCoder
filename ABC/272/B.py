n, m = map(int, input().split())
kx = list(list(map(int, input().split())) for _ in range(m))

check_list = [[False]*n for _ in range(n)]

for KX in kx:
    k = KX[0]
    x = KX[1:k+1]
    print(k, x)