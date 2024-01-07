a, b, c = map(int, list(input()))

abc = 100*a + 10*b + c
bca = 100*b + 10*c + a
cab = 100*c + 10*a + b

print(abc+bca+cab)
