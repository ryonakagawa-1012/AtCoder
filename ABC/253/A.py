def yes():
    print("Yes")


def no():
    print("No")


a, b, c = map(int, input().split())

if b == sorted([a, b, c])[1]:
    yes()
else:
    no()
