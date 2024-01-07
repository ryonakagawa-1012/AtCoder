M, D = map(int, input().split())

y, m, d = map(int, input().split())

ans_y = y
ans_m = m
ans_d = d+1

if D < ans_d:
    ans_d = 1
    ans_m += 1
if M < ans_m:
    ans_m = 1
    ans_y += 1

print(ans_y, ans_m, ans_d)
