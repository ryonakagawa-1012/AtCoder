N = int(input())
W = input().split()

# print(W)

if "and" in W or "not" in W or "that" in W or "the" in W or "you" in W:
    print("Yes")
else:
    print("No")

