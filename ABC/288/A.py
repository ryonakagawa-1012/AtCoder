N = int(input())
AB = list(list(map(int, input().split())) for _ in range(N))

for _ in AB:
    print(sum(_))
