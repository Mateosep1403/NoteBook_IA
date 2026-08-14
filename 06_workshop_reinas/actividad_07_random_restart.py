import random


N = 4


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


def hill_climbing(initial_state, max_steps=100):
    current = initial_state.copy()
    history = [current.copy()]

    for _ in range(max_steps):
        current_cost = cost(current)
        if current_cost == 0:
            break

        next_state, next_cost = best_neighbor(current)
        if next_cost >= current_cost:
            break

        current = next_state
        history.append(current.copy())

    return current, history


def random_state(n=N):
    return [random.randrange(n) for _ in range(n)]


def random_restart_hill_climbing(max_restarts=50, max_steps=100):
    best_state = None
    best_history = None
    best_cost = float("inf")

    for restart in range(max_restarts + 1):
        initial_state = random_state()
        final_state, history = hill_climbing(initial_state, max_steps)
        final_cost = cost(final_state)

        if final_cost < best_cost:
            best_state = final_state
            best_history = history
            best_cost = final_cost

        if final_cost == 0:
            return best_state, best_history, restart

    return best_state, best_history, max_restarts


best_state, best_history, restarts = random_restart_hill_climbing()

print("Mejor estado:", best_state)
print("Costo:", cost(best_state))
print("Reinicios utilizados:", restarts)
