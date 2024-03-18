def can_cover(H, W, tiles):
    grid = [[0]*W for _ in range(H)]
    for tile in tiles:
        for i in range(H):
            for j in range(W):
                if i + tile[0] <= H and j + tile[1] <= W:
                    for x in range(tile[0]):
                        for y in range(tile[1]):
                            if grid[i+x][j+y] == 1:
                                break
                        else:
                            continue
                        break
                    else:
                        for x in range(tile[0]):
                            for y in range(tile[1]):
                                grid[i+x][j+y] = 1
    return all(all(row) for row in grid)

n, h, w = sep_read(int)
    a = []
    b = []
    for _ in range(n):
        at, bt = sep_read(int)
        a.append(at)
        b.append(bt)

tiles = [(ai, bi) for ai, bi in zip(a, b)]
print(can_cover(h, w, tiles))