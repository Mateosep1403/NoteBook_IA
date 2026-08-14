def attacking(row_i, col_i, row_j, col_j):
    return row_i == row_j or abs(row_i - row_j) == abs(col_i - col_j)


assert attacking(0, 0, 0, 3) is True
assert attacking(0, 0, 3, 3) is True
assert attacking(0, 0, 1, 3) is False

print("Pruebas superadas.")
