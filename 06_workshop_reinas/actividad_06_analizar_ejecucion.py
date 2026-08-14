import random
import matplotlib.pyplot as plt


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


def plot_cost_history(history, title="Evolucion del costo"):
    costs = [cost(state) for state in history]

    plt.figure(figsize=(7, 4))
    plt.plot(range(len(costs)), costs, marker="o")
    plt.xlabel("Iteracion")
    plt.ylabel("Costo")
    plt.title(title)
    plt.xticks(range(len(costs)))
    plt.show()


_, history = hill_climbing([0, 0, 0, 0])
plot_cost_history(history)
