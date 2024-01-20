def count_gold_cells_optimized(M, N, K, actions):
    row_toggle = [False] * M
    col_toggle = [False] * N
    for action in actions:
        direction, index = action[0], int(action[1]) - 1
        if direction == 'R':
            row_toggle[index] = not row_toggle[index]
        else: 
            col_toggle[index] = not col_toggle[index]
    toggled_rows = sum(row_toggle)
    toggled_cols = sum(col_toggle)
    gold_cells = (toggled_rows * (N - toggled_cols)) + ((M - toggled_rows) * toggled_cols)
    return gold_cells
M = int(input())
N = int(input())
K = int(input())
actions = [input().split() for _ in range(K)]
gold_cells = count_gold_cells_optimized(M, N, K, actions)
print(gold_cells)