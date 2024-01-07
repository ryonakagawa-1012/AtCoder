N = int(input())
S = input()
T = input()

Similar_Flag = True

for i in range(N):
    if S[i] == T[i] or (S[i] == "l" and T[i] == "1") or (S[i] == "1" and T[i] == "l") or (S[i] == "o" and T[i] == "0") or (S[i] == "0" and T[i] == "o"):
        pass
    else:
        Similar_Flag = False

if Similar_Flag:
    print("Yes")
else:
    print("No")
