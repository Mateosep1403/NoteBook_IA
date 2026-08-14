import math
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


def random_state(n=N):
    return [random.randrange(n) for _ in range(n)]


def acceptance_probability(current_cost, candidate_cost, temperature):
    if candidate_cost <= current_cost:
        return 1.0
    if temperature <= 0:
        return 0.0
    return math.exp(-(candidate_cost - current_cost) / temperature)


def simulated_annealing(
    initial_state,
    initial_temperature=10.0,
    cooling_rate=0.95,
    min_temperature=1e-3,
    max_steps=1000,
):
    current = initial_state.copy()
    best_state = current.copy()
    temperature = initial_temperature
    history = [current.copy()]
    temperatures = [temperature]

    for _ in range(max_steps):
        if cost(best_state) == 0 or temperature < min_temperature:
            break

        candidate = random.choice(neighbors(current))
        current_cost = cost(current)
        candidate_cost = cost(candidate)
        probability = acceptance_probability(current_cost, candidate_cost, temperature)

        if random.random() < probability:
            current = candidate
            history.append(current.copy())
            temperatures.append(temperature)

            if candidate_cost < cost(best_state):
                best_state = candidate.copy()

        temperature *= cooling_rate

    return best_state, history, temperatures


initial_state = random_state()
sa_state, sa_history, temperatures = simulated_annealing(initial_state)

print("Estado inicial:", initial_state)
print("Mejor estado:", sa_state)
print("Costo final:", cost(sa_state))
print("Estados aceptados:", len(sa_history))
