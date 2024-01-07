def main():
    from builtins import int, map, abs
    from sys import stdin

    readline = stdin.readline()

    x, y = map(int, readline.split())

    if -2 <= x-y <= 3:
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    main()
