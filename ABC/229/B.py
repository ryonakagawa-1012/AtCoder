a, b = input().split()

len_max = max(len(a), len(b))

a = list(a.zfill(len_max))
b = list(b.zfill(len_max))

for i in range(len_max):
    if int(a[i]) + int(b[i]) >= 10:
        print("Hard")
        exit()

print("Easy")
