from geneticmodel.fitness import fitness
def average_fitness(population,data2, userID):
    max = 0
    maxIndex = 0
    avg = 0
    index = 0
    for chromosome in population:
        temp =  fitness(chromosome,data2,userID)
        avg += temp
        max = temp if temp>max else max
        maxIndex = index if temp>max else maxIndex
        index +=1
    return [avg/len(population),max,maxIndex]