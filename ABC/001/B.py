m = int(input())/1000

if m < 0.1:
    print(00)
elif 0.1 <= m < 1:
    print("".join(["0", str(int(m*10))]))
elif 1 <= m <= 5:
    print(int(m*10))
elif 6 <= m <= 30:
    print(int(m+50))
elif 35 <= m <= 70:
    print(int((m-30)/5)+80)
elif 70 < m:
    print(89)
