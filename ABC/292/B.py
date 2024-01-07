N, Q = map(int, input().split())
event = list(list(map(int, input().split())) for _ in range(Q))

penalty = [0]*N

for i in range(Q):
    if event[i][0] == 1:
        penalty[event[i][1]-1] += 1

    elif event[i][0] == 2:
        penalty[event[i][1]-1] += 2

    elif event[i][0] == 3:
        if penalty[event[i][1]-1] < 2:
            print("No")
        else:
            print("Yes")
