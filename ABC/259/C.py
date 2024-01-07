def yes():
    print("Yes")


def no():
    print("No")


def main():
    from sys import stdin
    from itertools import groupby

    readline = stdin.readline

    s = readline().rstrip()
    t = readline().rstrip()

    flag = True

    if s == t:
        pass
    else:
        compression_s = [(k, len(list(g))) for k, g in groupby(s)]
        compression_t = [(k, len(list(g))) for k, g in groupby(t)]
        # print(compression_s)
        # print(compression_t)
        compression_s_len = len(compression_s)
        compression_t_len = len(compression_t)
        if compression_s_len == compression_t_len:
            for i in range(compression_s_len):
                compare_s = compression_s[i]
                compare_t = compression_t[i]

                if compare_s == compare_t:
                    pass
                elif compare_s[0] != compare_t[0]:
                    flag = False
                    break
                elif compare_s[1] <= compare_t[1] and 3 <= compare_t[1]:
                    pass
                else:
                    # print(compare_s, compare_t)
                    flag = False
                    break

        else:
            flag = False

    if flag:
        yes()
    else:
        no()


if __name__ == "__main__":
    main()
