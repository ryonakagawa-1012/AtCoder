

# Read the input
n = int(input())
cards = [tuple(map(int, input().split())) for _ in range(n)]

print(cards)

# Solve the problem
result = solve(n, cards)

# Print the result
for card in result:
    print(card)