N = list(map(str, input()))

size = len(N)

Flag = 0

for i in range(size-1):
    if N[i] <= N[i+1]:
        Flag = 1

if Flag == 1:
    print("No")
else:
    print("Yes")
