import sys
from sortedcontainers import SortedList

def main():
    n, l = map(int, sys.stdin.readline().split())
    d = list(map(int, sys.stdin.readline().split()))
    player_to_dist = {i + 1: d[i] for i in range(n)}
    dist_to_player = {d[i]: i + 1 for i in range(n)}
    q = int(input())
    d = SortedList(d)
    dist = 0
    for _ in range(q):
        query = input()
        if query[0] == "1":
            que, x, m = map(int, query.split())
            # print(x, m)
            d.discard(player_to_dist[x])
            d.add(player_to_dist[x] + m)
            dist_to_player.pop(player_to_dist[x])
            dist_to_player[player_to_dist[x] + m] = x
            player_to_dist[x] = player_to_dist[x] + m
        else:
            for i in range(1, 6):
                print(dist_to_player[d[-i]], d[-i] + dist)

        dist += l

if __name__ == '__main__':
    main()
