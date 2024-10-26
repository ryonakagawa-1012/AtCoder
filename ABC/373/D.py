import sys
from collections import defaultdict, deque

def input(): return sys.stdin.readline().rstrip()

sys.setrecursionlimit(10 ** 6)

def dfs(start, graph, x):
    stack = deque([(start, 0)])
    while stack:
        v, value = stack.pop()
        if x[v] is not None:
            continue
        x[v] = value
        for next_v, w in graph[v]:
            if x[next_v] is None:
                stack.append((next_v, value + w))

def main():
    n, m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, -w))

    x = [None] * (n + 1)

    for v in range(1, n + 1):
        if x[v] is None:
            dfs(v, graph, x)

    print(" ".join(map(str, x[1:])))

if __name__ == "__main__":
    main()
