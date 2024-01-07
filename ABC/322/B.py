N, M = map(int, input().split())

S = input()

T = input()

if T[0:N] == S and T[M-N:] == S:
    print(0)
elif T[0:N] == S:
    print(1)
elif T[M-N:] == S:
    print(2)
else:
    print(3)
