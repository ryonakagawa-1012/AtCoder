from sys import stdin


def yes():
    print("Yes")


def no():
    print("No")


def takahashi():
    print("Takahashi")


def aoki():
    print("Aoki")


def sep_read(types=str):
    if types == str:
        return stdin.readline().split()
    else:
        return map(types, stdin.readline().split())


def main():
    s = input()

    cond1 = False
    cond2 = False
    cond3 = False

    for S in s:
        if S.isupper():
            cond1 = True
        if S.islower():
            cond2 = True

    if len(s) == len(set(s)):
        cond3 = True

    if all([cond1, cond2, cond3]):
        yes()
    else:
        no()


if __name__ == "__main__":
    main()
