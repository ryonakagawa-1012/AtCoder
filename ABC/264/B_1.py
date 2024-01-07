r, c = map(int, input().split())
print("white" if max(abs(r-8), abs(c-8)) % 2 == 0 else "black")
