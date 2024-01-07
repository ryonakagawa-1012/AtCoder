n =  int(input())
s = list(map(ord, input()))

for i in range(n-1):
    if (chr(s[i]) == "a" or (chr(s[i]) == "b")) and (s[i]+1 == s[i+1] or s[i]-1 == s[i+1]):
        print("Yes")
        exit()

print("No"