k = int(input())
print("21:"+"{:02}".format(k) if k < 60 else "22:"+"{:02}".format(k-60))
