from sys import stdin


def yes():
    print("Yes")


def no():
    print("No")


def takahashi():
    print("Takahashi")


def aoki():
    print("Aoki")


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


def main():
    from bisect import bisect_left

    n, k = sep_read(int)
    a = list(sep_read(int))

    a_f = a[:n//2]
    a_b = a[n//2:]

    a_f_sum = bit_full_search(a_f, len(a_f))
    a_b_sum = bit_full_search(a_b, len(a_b))

    # print(a_f_sum)
    # print(a_b_sum)

    a_b_sum.sort()
    len_a_b_sum = len(a_b_sum)

    for i in range(len(a_f_sum)):
        index = bisect_left(a_b_sum, k-a_f_sum[i])
        if index < len_a_b_sum and a_b_sum[index] == k-a_f_sum[i]:
            yes()
            exit()

    no()


if __name__ == "__main__":
    main()
