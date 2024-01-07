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
    n, k = sep_read(int)
    a = list(sep_read(int))

    ans = 0

    if k % 2 == 0:
        for i in range(0, k, 2):
            ans += abs(a[i] - a[i+1])
    else:
        if len(a) != 1:
            before = [0]
            after = [0]
            for i in range(0, k-1, 2):
                # print(i)
                before.append(abs(a[i] - a[i+1]) + before[-1])
                after.append(abs(a[k-i-1] - a[k-i-2]) + after[-1])
            del before[0], after[0]
            # print(before)
            # print(after)
            ans = before[-1]
            for i in range(k//2):
                ans = min(ans, before[-i]+after[i])

    print(ans)


if __name__ == "__main__":
    main()
