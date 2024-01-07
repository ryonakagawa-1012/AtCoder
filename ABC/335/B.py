from sys import stdin


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
    n = int(input())

    for x in range(22):
        for y in range(22):
            for z in range(22):
                if x + y + z <= n:
                    print(x, y, z)


if __name__ == "__main__":
    main()
