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
    t = input()

    direction = "e"

    x, y = 0, 0

    for T in t:
        if T == "S":
            if direction == "e":
                x += 1
            elif direction == "s":
                y -= 1
            elif direction == "w":
                x -= 1
            elif direction == "n":
                y += 1
        else:
            if direction == "e":
                direction = "s"

            elif direction == "s":
                direction = "w"

            elif direction == "w":
                direction = "n"

            elif direction == "n":
                direction = "e"

    print(x, y)


if __name__ == "__main__":
    main()
