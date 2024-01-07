n = int(input())
s = input()

for i in range(1, n):
    count = 0
    for j in range(n):
        if i+j < n:
            if s[j] != s[j+i]:
                count += 1
            else:
                break
        else:
            break
    print(count)
