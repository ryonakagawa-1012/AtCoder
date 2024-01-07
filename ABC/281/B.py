S = input()

if S[:1].isalpha() and S[-1:].isalpha() and S[1:-1].isdecimal():
    if int(S[1]) != 0 and 100000 <= int(S[1:-1]) <= 999999:
        print("Yes")
        exit()

print("No")
