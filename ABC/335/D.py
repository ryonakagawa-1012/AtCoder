from sys import stdin


def yes():
    print("Yes")


def no():
    print("No")


def y_or_n(yes_cond):
    print("Yes" if yes_cond else "No")


def a_to_z():
    return list(chr(ord("a")+i) for i in range(26))


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

    for i in range(2**n):
        s_u_m = 0
        for j in range(n):
            bit = (2 ** j)
            if (i // bit) % 2 == 1:
                s_u_m += lst[j]
        ans.append(s_u_m)

    return ans


def main():
    n = int(readline())
    grid = (list([None]*n for _ in range(n)))

    num = 1
    top, bottom, left, right = 0, n-1, 0, n-1

    while num <= n * n:
        for i in range(left, right+1):
            grid[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom+1):
            grid[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left-1, -1):
            grid[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top-1, -1):
            grid[i][left] = num
            num += 1
        left += 1

    grid[n//2][n//2] = "T"

    for grid_t in grid:
        print(*grid_t, sep="\n")


if __name__ == "__main__":
    main()
