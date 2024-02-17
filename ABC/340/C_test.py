import heapq

def solve(n):
    q = [-n]
    total = 0
    while q:
        x = -heapq.heappop(q)
        total += x
        if x > 1:
            heapq.heappush(q, -x // 2)
            heapq.heappush(q, -(x - x // 2))
    return total

print(solve(int(input())))