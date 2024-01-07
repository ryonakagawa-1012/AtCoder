from sys import stdin


def yes():
    print("Yes")


def no():
    print("No")


def sep_read(types=str):
    if types == str:
        return stdin.readline().split()
    else:
        return map(types, stdin.readline().split())


def main():
    n, m = sep_read(int)
    s = list(input())

    t_sum = m
    logo_t = 0
    buy_count = 0

    for S in map(int, s):
        if S == 0:
            t_sum = m
            logo_t = buy_count
        elif S == 1:
            if t_sum != 0:
                t_sum -= 1
            elif logo_t != 0:
                logo_t -= 1
            else:
                buy_count += 1
        else:
            if logo_t == 0:
                buy_count += 1
            else:
                logo_t -= 1

    print(buy_count)


if __name__ == "__main__":
    main()
