S = list(map(int, input()))

No_Flag = False

for i in range(16):
    if (i+1) % 2 == 0 and S[i] != 0:
        No_Flag = True

if No_Flag:
    print("No")
else:
    print("Yes")
