n = int(input())
d = list(map(int, input().split()))

ans = 0

for month in range(1, n+1):
    for day in range(1, d[month-1]+1):
        tmp = str(month) + str(day)
        if len(tmp) == 2 and tmp == tmp[::-1]:
            ans += 1
        elif len(tmp) == 3 and tmp[2] == tmp[1] == tmp[0]:
            ans += 1
        elif len(tmp) == 4 and tmp[3] == tmp[2] == tmp[1] == tmp[0]:
            ans+= 1
print(ans)
