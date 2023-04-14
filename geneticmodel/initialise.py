import random

#while loop control variable
def initialise(pop_size,lchrom, lact):
    limit=0
    #create an empty population
    population = []
    while limit!=pop_size:
        #initialise the chromosome
        tchromosome = [-1 for i in range(lchrom)]
        #generate a random string
        temp_indices = set([i for i in range(0,lact)])
        temp_indices.add(-1)
        for i in range(lchrom):
            value = random.choice(list(temp_indices))
            tchromosome[i] = value if value!=-1 else -1
            if tchromosome[i]!=-1:
                temp_indices.remove(tchromosome[i])

        #append this individual to the population
        population.append(tchromosome)
        #incrment the population limit
        limit+=1
    return population