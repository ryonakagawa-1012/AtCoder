N = int(input())
S = [input() for _ in range(N)]
SS = S.copy()
Flag = True
for s in S:
    SS.remove(s)
    if not (s[0] == "H" or s[0] == "D" or s[0] == "C" or s[0] == "S") or not (s[1] == "A" or s[1] == "T" or s[1] == "J" or s[1] == "Q" or s[1] == "K" or "2" <= s[1] <= "9") or s in SS:
        Flag = False
    if not Flag:
        break

if Flag:
    print("Yes")
else:
    print("No")
