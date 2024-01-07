N = int(input())
S = input()

Flag = True

for i in range(N-1):
    if S[i] == "M" and S[i+1] == "M":
        Flag = False
        break
    if S[i] == "F" and S[i+1] == "F":
        Flag = False
        break

if Flag:
    print("Yes")
else:
    print("No")
