def main():
    from builtins import print
    from sys import stdin

    readline = stdin.readline

    n = int(readline())
    s = readline()

    tmp = ""
    ans = {}

    for i in range(n+1):
        tmp = tmp + s[i]
        if i > 0 and s[i-1] != s[i]:
            count = len(tmp)-1
            if tmp[0] in ans:
                if ans[tmp[0]] < count:
                    ans[tmp[0]] = count
            else:
                ans[tmp[0]] = count
            tmp = s[i]
    #     print(tmp)
    #
    # print(ans)
    print(sum(ans.values()))


if __name__ == "__main__":
    main()
