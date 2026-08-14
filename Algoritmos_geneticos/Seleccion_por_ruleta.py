import random


def fitness(individual):
    return sum(individual)


def roulette_selection(population, rng):
    fitnesses = [fitness(ind) for ind in population]
    total_fitness = sum(fitnesses)

    if total_fitness == 0:
        return rng.choice(population).copy()

    pick = rng.uniform(0, total_fitness)
    accumulated = 0

    for individual, fit in zip(population, fitnesses):
        accumulated += fit

        if pick <= accumulated:
            return individual.copy()

    return population[-1].copy()


rng = random.Random(14)

population = [
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0]
]

selected = roulette_selection(population, rng)

print("Población:")
for individual in population:
    print(individual)

print("\nIndividuo seleccionado:")
print(selected)