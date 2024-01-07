grid = ["bbbbbbbbbbbbbbb",
        "b.............b",
        "b.bbbbbbbbbbb.b",
        "b.b.........b.b",
        "b.b.bbbbbbb.b.b",
        "b.b.b.....b.b.b",
        "b.b.b.bbb.b.b.b",
        "b.b.b.b.b.b.b.b",
        "b.b.b.bbb.b.b.b",
        "b.b.b.....b.b.b",
        "b.b.bbbbbbb.b.b",
        "b.b.........b.b",
        "b.bbbbbbbbbbb.b",
        "b.............b",
        "bbbbbbbbbbbbbbb"]

r, c = map(int, input().split())

print("black" if grid[r-1][c-1] == "b" else "white")
