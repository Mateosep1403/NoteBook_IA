import random


def uniform_crossover(parent1, parent2, crossover_rate, rng):
  
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



rng = random.Random(14)

parent1 = [1, 1, 1, 1, 1, 1, 1, 1]
parent2 = [0, 0, 0, 0, 0, 0, 0, 0]

child1, child2 = uniform_crossover(
    parent1,
    parent2,
    crossover_rate=1.0,
    rng=rng
)

print("Padre 1:", parent1)
print("Padre 2:", parent2)
print("Hijo 1:  ", child1)
print("Hijo 2:  ", child2)