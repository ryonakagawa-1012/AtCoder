p, q = input().split()

ABCDEFG = {"A": 3, "B": 1, "C": 4, "D": 1, "E": 5, "F": 9}

ans = 0

for i in range(min(ord(p), ord(q)), max(ord(p), ord(q))):
    ans += ABCDEFG[chr(i)]

print(ans)
