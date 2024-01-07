def main():
    from builtins import int, str, range
    from sys import stdin

    readline = stdin.readline()

    n = int(readline)

    for i in range(n, 920):
        if int(str(i)[0]) * int(str(i)[1]) == int(str(i)[2]):
            print(i)
            exit()


if __name__ == "__main__":
    main()
