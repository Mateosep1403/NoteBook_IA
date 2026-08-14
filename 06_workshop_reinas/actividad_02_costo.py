def attacking(row_i, col_i, row_j, col_j):
    return row_i == row_j or abs(row_i - row_j) == abs(col_i - col_j)


def cost(state):
    total = 0
    for col_i in range(len(state)):
        for col_j in range(col_i + 1, len(state)):
            if attacking(state[col_i], col_i, state[col_j], col_j):
                total += 1
    return total


assert cost([0, 0, 0, 0]) == 6
assert cost([0, 1, 2, 3]) == 6
assert cost([1, 3, 0, 2]) == 0

print("Pruebas superadas.")
