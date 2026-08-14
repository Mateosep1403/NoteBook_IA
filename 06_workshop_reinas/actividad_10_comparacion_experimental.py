import math
import random


N = 4
SEED = 42
random.seed(SEED)


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


def compare_algorithms(trials=100):
    results = {
        "Hill Climbing": 0,
        "Random Restart": 0,
        "Simulated Annealing": 0,
    }

    for _ in range(trials):
        initial_state = random_state()

        hc_state, _ = hill_climbing(initial_state)
        if cost(hc_state) == 0:
            results["Hill Climbing"] += 1

        rr_state, _, _ = random_restart_hill_climbing(max_restarts=20)
        if cost(rr_state) == 0:
            results["Random Restart"] += 1

        sa_state, _, _ = simulated_annealing(initial_state)
        if cost(sa_state) == 0:
            results["Simulated Annealing"] += 1

    return results


results = compare_algorithms(trials=100)
for algorithm, successes in results.items():
    print(f"{algorithm:20s}: {successes}/100")
