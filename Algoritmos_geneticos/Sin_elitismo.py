import random
import numpy as np


SEED = 14


def create_individual(length, rng):
    return [rng.randint(0, 1) for _ in range(length)]


def fitness(individual):
    return sum(individual)


def as_string(individual):
    return ''.join(map(str, individual))


def tournament_selection(population, tournament_size, rng):
    contestants = rng.sample(population, tournament_size)
    return max(contestants, key=fitness).copy()


def one_point_crossover(parent1, parent2, crossover_rate, rng):
    if rng.random() >= crossover_rate:
        return parent1.copy(), parent2.copy()

    point = rng.randint(1, len(parent1) - 1)

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2


def mutate(individual, mutation_rate, rng):
    child = individual.copy()

    for i in range(len(child)):
        if rng.random() < mutation_rate:
            child[i] = 1 - child[i]

    return child


def genetic_algorithm(
    chromosome_length=40,
    population_size=60,
    generations=100,
    crossover_rate=0.9,
    mutation_rate=None,
    tournament_size=3,
    elitism=True,
    seed=0
):

    if mutation_rate is None:
        mutation_rate = 1 / chromosome_length

    rng = random.Random(seed)

    population = [
        create_individual(chromosome_length, rng)
        for _ in range(population_size)
    ]

    history = []

    for generation in range(generations + 1):

        fitnesses = [
            fitness(individual)
            for individual in population
        ]

        best_index = int(np.argmax(fitnesses))
        best = population[best_index].copy()

        history.append({
            "generation": generation,
            "best": max(fitnesses),
            "mean": float(np.mean(fitnesses)),
            "diversity": len({
                tuple(ind)
                for ind in population
            }) / population_size,
            "best_individual": best
        })

        if fitness(best) == chromosome_length:
            break

        new_population = [best] if elitism else []

        while len(new_population) < population_size:

            parent1 = tournament_selection(
                population,
                tournament_size,
                rng
            )

            parent2 = tournament_selection(
                population,
                tournament_size,
                rng
            )

            child1, child2 = one_point_crossover(
                parent1,
                parent2,
                crossover_rate,
                rng
            )

            child1 = mutate(
                child1,
                mutation_rate,
                rng
            )

            child2 = mutate(
                child2,
                mutation_rate,
                rng
            )

            new_population.extend([child1, child2])

        population = new_population[:population_size]

    return history[-1]["best_individual"], history


# Con
best_elite, history_elite = genetic_algorithm(
    chromosome_length=40,
    population_size=60,
    generations=100,
    crossover_rate=0.9,
    mutation_rate=None,
    tournament_size=3,
    elitism=True,
    seed=SEED
)


# Sin

best_no_elite, history_no_elite = genetic_algorithm(
    chromosome_length=40,
    population_size=60,
    generations=100,
    crossover_rate=0.9,
    mutation_rate=None,
    tournament_size=3,
    elitism=False,
    seed=SEED
)




print("===== CON ELITISMO =====")
print("Mejor individuo:", as_string(best_elite))
print("Fitness final:", fitness(best_elite), "/", len(best_elite))
print("Generaciones:", history_elite[-1]["generation"])


print("\n===== SIN ELITISMO =====")
print("Mejor individuo:", as_string(best_no_elite))
print("Fitness final:", fitness(best_no_elite), "/", len(best_no_elite))
print("Generaciones:", history_no_elite[-1]["generation"])




print("\n EVOLUCIÓN DEL MEJOR FITNESS ")

print("\nCon elitismo:")
for i in range(1, len(history_elite)):
    anterior = history_elite[i - 1]["best"]
    actual = history_elite[i]["best"]

    print(
        f"Generación {i-1} -> {i}: "
        f"{anterior} -> {actual}"
    )


print("\nSin elitismo:")
for i in range(1, len(history_no_elite)):
    anterior = history_no_elite[i - 1]["best"]
    actual = history_no_elite[i]["best"]

    if actual < anterior:
        print(
            f"DISMINUYÓ: Generación {i-1} -> {i}: "
            f"{anterior} -> {actual}"
        )