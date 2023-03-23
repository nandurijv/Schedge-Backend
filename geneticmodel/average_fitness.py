from geneticmodel.fitness import fitness
def average_fitness(population):
    max = 0
    maxIndex = 0
    avg = 0
    index = 0
    for chromosome in population:
        temp =  fitness(chromosome)
        avg += temp
        max = temp if temp>max else max
        maxIndex = index if temp>max else maxIndex
        index +=1
    return [avg/len(population),max,maxIndex]