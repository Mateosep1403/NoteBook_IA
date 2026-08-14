import random
import numpy as np


target = "INTELIGENCIA ARTIFICIAL"

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")


def create_phrase_individual(length, rng):
    return [rng.choice(alphabet) for _ in range(length)]


def phrase_fitness(individual, target):
    return sum(
        character == target[i]
        for i, character in enumerate(individual)
    )


def mutate_phrase(individual, mutation_rate, rng):
    child = individual.copy()

    for i in range(len(child)):
        if rng.random() < mutation_rate:
            child[i] = rng.choice(alphabet)

    return child


def phrase_tournament_selection(population, tournament_size, target, rng):
    contestants = rng.sample(population, tournament_size)

    return max(
        contestants,
        key=lambda individual: phrase_fitness(individual, target)
    ).copy()


def phrase_crossover(parent1, parent2, crossover_rate, rng):
    if rng.random() >= crossover_rate:
        return parent1.copy(), parent2.copy()

    child1 = []
    child2 = []

    for gene1, gene2 in zip(parent1, parent2):

        if rng.random() < 0.5:
            child1.append(gene1)
            child2.append(gene2)
        else:
            child1.append(gene2)
            child2.append(gene1)

    return child1, child2


def genetic_phrase(
    target,
    population_size=100,
    generations=500,
    crossover_rate=0.9,
    mutation_rate=0.05,
    tournament_size=3,
    elitism=True,
    seed=14
):

    rng = random.Random(seed)

    
    population = [
        create_phrase_individual(len(target), rng)
        for _ in range(population_size)
    ]

    history = []

    for generation in range(generations + 1):

        
        fitnesses = [
            phrase_fitness(individual, target)
            for individual in population
        ]

        best_index = int(np.argmax(fitnesses))
        best = population[best_index].copy()
        best_fitness = fitnesses[best_index]

        history.append({
            "generation": generation,
            "best": best_fitness,
            "best_individual": best.copy()
        })

        
        if best_fitness == len(target):
            break

        
        new_population = [best] if elitism else []

        while len(new_population) < population_size:

            
            parent1 = phrase_tournament_selection(
                population,
                tournament_size,
                target,
                rng
            )

            parent2 = phrase_tournament_selection(
                population,
                tournament_size,
                target,
                rng
            )

          
            child1, child2 = phrase_crossover(
                parent1,
                parent2,
                crossover_rate,
                rng
            )

           
            child1 = mutate_phrase(
                child1,
                mutation_rate,
                rng
            )

            child2 = mutate_phrase(
                child2,
                mutation_rate,
                rng
            )

            new_population.extend([child1, child2])

        population = new_population[:population_size]

    return best, history



best_phrase, phrase_history = genetic_phrase(
    target="INTELIGENCIA ARTIFICIAL",
    population_size=100,
    generations=500,
    crossover_rate=0.9,
    mutation_rate=0.05,
    tournament_size=3,
    elitism=True,
    seed=14
)

print("Frase encontrada:", ''.join(best_phrase))
print(
    "Fitness:",
    phrase_fitness(best_phrase, "INTELIGENCIA ARTIFICIAL"),
    "/",
    len("INTELIGENCIA ARTIFICIAL")
)
print(
    "Generaciones:",
    phrase_history[-1]["generation"]
)