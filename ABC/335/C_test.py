from sys import stdin
from collections import deque

def yes():
    print("Yes")


def no():
    print("No")

def y_or_n(yes_cond):
    print("Yes" if yes_cond else "No")

def a_to_z():
    return list(chr(ord("a") + i) for i in range(26))

def atcoder():
    return list("atcoder")

def takahashi():
    print("Takahashi")

def aoki():
    print("Aoki")

def readline(back_slash=False):
    if back_slash:
        return stdin.readline()
    else:
        return stdin.readline().rstrip()

def sep_read(types=str):
    if types == str:
        return stdin.readline().rstrip().split()
    else:
        return map(types, stdin.readline().split())

def bit_full_search(lst, n):
    ans = []

    for i in range(2 ** n):
        s_u_m = 0
        for j in range(n):
            bit = (2 ** j)
            if (i // bit) % 2 == 1:
                s_u_m += lst[j]
        ans.append(s_u_m)

    return ans

def main():
    n, q = sep_read(int)
    dragon_x = deque([i for i in range(1, n+1)])
    dragon_y = deque([0]*n)

    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    for _ in range(q):
        num, direction = sep_read()
        if num == "1":
            dx, dy = directions[direction]
            dragon_x[0] += dx
            dragon_y[0] += dy
        else:
            print(dragon_x[int(direction)-1], dragon_y[int(direction)-1])

if __name__ == "__main__":
    main()