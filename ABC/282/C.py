def main():
    from builtins import print, int, range, list
    from sys import stdin

    readline = stdin.readline

    n = int(readline())
    s = list(readline())

    is_surrounded = False
    count_double_quotation = 0

    for i in range(n):
        if s[i] == "\"":
            count_double_quotation += 1
        if count_double_quotation % 2 == 0 and s[i] == ",":
            s[i] = "."

    print("".join(s))

if __name__ == "__main__":
    main()
