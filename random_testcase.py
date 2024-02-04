from random import randint
N = randint(1, 10000)
D = randint(1, 10000)
A = [randint(1, 10000) for i in range(N)]
print(N, D)
print(*A)