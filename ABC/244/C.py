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
    n = int(input())

    inputted = None
    declared = []

    while inputted != 0:
        for i in range(1, 2*n+2):
            if i not in declared:
                print(i)
                declared.append(i)
                break
        inputted = int(input())
        declared.append(inputted)


if __name__ == "__main__":
    main()
