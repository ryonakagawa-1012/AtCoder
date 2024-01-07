from pprint import pprint

H, W = map(int, input().split())
S = list(input() for _ in range(H))
pprint(S, width=20)

sensor_list = [(i+1, j+1) for i in range(H) for j in range(W) if S[i][j] == "#"]
print(sensor_list)