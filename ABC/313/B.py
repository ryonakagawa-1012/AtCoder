N, M = map(int, input().split())

AB = [list(map(int, input().split())) for _ in range(M)]

A = set([a[0] for a in AB])
B = set([b[1] for b in AB])

Gojo_Satoru = A - B

# print(Gojo_Satoru)

if len(Gojo_Satoru) == 1:
    print("".join((str(_) for _ in Gojo_Satoru)))
else:
    print(-1)
