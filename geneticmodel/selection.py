import random

def roulette_wheel_selection(population, fitness_fn, num_parents,data,userID):
    # Calculate fitness scores for each individual in the population
    fitness_scores = []
    for i in range(len(population)):
        temp = fitness_fn(population[i],data,userID)
        fitness_scores.append(temp)
    # Calculate the sum of all fitness scores
    total_fitness = sum(fitness_scores)
    # Calculate the relative fitness for each individual
    relative_fitness = [fitness_score / total_fitness if total_fitness!=0 else 0.5 for fitness_score in fitness_scores]

    # Select the top 'num_parents' individuals using roulette wheel selection
    parents = []
    for i in range(num_parents):
        # Spin the roulette wheel to select an individual
        r = random.uniform(0, 1)
        spin = 0
        for j in range(len(relative_fitness)):
            spin += relative_fitness[j]
            if spin > r:
                parents.append(j)
                break
    return parents