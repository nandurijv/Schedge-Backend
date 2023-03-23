from geneticmodel.decode import decode
def fitness(x):
    y = x.copy()
    decoded_chromosome = decode(y)
    fitness = sum(decoded_chromosome)
    return fitness