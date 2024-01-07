from sys import stdin


def yes():
    print("Yes")


def no():
    print("No")


def y_or_n(yes_cond):
    print("Yes" if yes_cond else "No")


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
    n, x = sep_read(int)
    a = [0] + list(sep_read(int))

    know = set()

    i = None

    ans = 1

    while True:
        if not know:
            know.add(x)
            i = x

        i = a[i]

        if i not in know:
            know.add(i)
            ans += 1
        else:
            break

    print(ans)


if __name__ == "__main__":
    main()
