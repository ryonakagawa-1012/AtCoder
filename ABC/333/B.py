from sys import stdin


def yes():
    print("Yes")


def no():
    print("No")


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


def main():
    s = list(input())
    t = list(input())

    s_len = abs(ord(s[1]) - ord(s[0]))
    t_len = abs(ord(t[1]) - ord(t[0]))

    if (s[0] == "A" and s[1] == "E") or (s[0] == "E" and s[1] == "A"):
        s_len = 1
    if (t[0] == "A" and t[1] == "E") or (t[0] == "E" and t[1] == "A"):
        t_len = 1

    if s_len == t_len == 1:
        yes()
    elif s_len >= 2 and t_len >= 2:
        yes()
    else:
        no()


if __name__ == "__main__":
    main()

