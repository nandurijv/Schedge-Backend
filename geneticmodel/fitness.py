from geneticmodel.decode import decode
def fitness(x,data,userID):
    y = x.copy()
    # print("ORIGINAL CHROMOSOME: ",y)
    decoded_chromosome = decode(y,data,userID)
    # print("DECODED CHROMOSOME:",decoded_chromosome)
    fitness = sum(decoded_chromosome)
    return fitness