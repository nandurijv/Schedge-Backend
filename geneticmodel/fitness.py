from geneticmodel.decode import decode
def fitness(x,data,userID):
    y = x.copy()
    decoded_chromosome = decode(y,data,userID)
    fitness = sum(decoded_chromosome)
    return fitness