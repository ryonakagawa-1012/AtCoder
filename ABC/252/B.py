from sys import stdin


def yes():
    print("Yes")


def no():
    print("No")


def sep_read(type_is=str):
    if type_is == str:
        return stdin.readline().split()
    else:
        return map(type_is, stdin.readline().split())


def main():

    n, k = sep_read()
    a = list(sep_read(int))
    b = list(sep_read(int))

    a_max_list = [index+1 for index, num in enumerate(a) if num == max(a)]

    # print(a_max_list)

    if len(set(a_max_list) & set(b)) != 0:
        yes()
    else:
        no()


if __name__ == "__main__":
    main()
