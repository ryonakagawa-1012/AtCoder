def yes():
    print("Yes")


def no():
    print("No")


abcde = sorted(list(map(int, input().split())))

# print(abcde)

if (abcde[0] == abcde[2] and abcde[3] == abcde[4]) or (abcde[0] == abcde[1] and abcde[2] == abcde[4]):
    yes()
else:
    no()
