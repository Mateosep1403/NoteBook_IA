import random


def attacking(row_i, col_i, row_j, col_j):
    return row_i == row_j or abs(row_i - row_j) == abs(col_i - col_j)


def cost(state):
    total = 0
    for col_i in range(len(state)):
        for col_j in range(col_i + 1, len(state)):
            if attacking(state[col_i], col_i, state[col_j], col_j):
                total += 1
    return total


def neighbors(state):
    result = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if row != state[col]:
                neighbor = state.copy()
                neighbor[col] = row
                result.append(neighbor)
    return result


def best_neighbor(state):
    candidates = neighbors(state)
    min_cost = min(cost(candidate) for candidate in candidates)
    best_candidates = [candidate for candidate in candidates if cost(candidate) == min_cost]
    return random.choice(best_candidates), min_cost


state = [0, 0, 0, 0]
next_state, next_cost = best_neighbor(state)

assert next_state in neighbors(state)
assert next_cost == cost(next_state)
assert next_cost == min(cost(s) for s in neighbors(state))

print("Pruebas superadas.")
