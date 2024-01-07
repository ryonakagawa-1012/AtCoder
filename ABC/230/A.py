s = int(input())
print("AGC" + str(s).zfill(3) if int(s) < 42 else "AGC" + str(s+1).zfill(3))
