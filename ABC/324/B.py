N = int(input())

if N == 1:
    print("Yes")
else:
    while N % 2 == 0:
        N //= 2
        print(N)
    while N % 3 == 0:
        N //= 3
        print(N)

    if N == 1:
        print("Yes")
    else:
        print("No")
