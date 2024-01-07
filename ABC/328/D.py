def main():
    from builtins import print
    from sys import stdin

    readline = stdin.readline

    s = readline().rstrip()

    ans = []

    for S in s:
        ans.append(S)
        # print(ans)
        # print("".join(ans[-3:]) == "ABC")
        if "".join(ans[-3:]) == "ABC":
            del ans[-3:]

    print("".join(ans))

if __name__ == "__main__":
    main()
