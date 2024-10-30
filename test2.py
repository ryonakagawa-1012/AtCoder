def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())

    rows = set()
    cols = set()
    diag1 = set()
    diag2 = set()

    for _ in range(M):
        a, b = map(int, input().split())
        rows.add(a)
        cols.add(b)
        diag1.add(a + b)
        diag2.add(a - b)

    # Total number of cells in the grid
    total_cells = N * N

    # Number of unsafe cells
    unsafe_cells = len(rows) * N + len(cols) * N + len(diag1) + len(diag2)

    # Subtract the overcounted cells (intersections)
    unsafe_cells -= len(rows) * len(cols)
    unsafe_cells -= len(rows) * len(diag1)
    unsafe_cells -= len(rows) * len(diag2)
    unsafe_cells -= len(cols) * len(diag1)
    unsafe_cells -= len(cols) * len(diag2)

    # Calculate the number of safe cells
    safe_cells = total_cells - unsafe_cells

    print(safe_cells)

if __name__ == "__main__":
    main()