n = int(input())
a = list(input() for _ in range(n))

flag = True

for y in range(n):
    for x in range(n):
        if a[x][y] == "W" and a[y][x] != "L":
            flag = False
        if a[x][y] == "L" and a[y][x] != "W":
            flag = False
        if a[x][y] == "D" and a[y][x] != "D":
            flag = False

if flag:
    print("correct")
else:
    print("incorrect")
