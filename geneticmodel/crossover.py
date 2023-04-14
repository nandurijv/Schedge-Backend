from geneticmodel.flip import biased_coin_flip as flip
from geneticmodel.mutation import mutation
import random

def crossover(parent1, parent2, lchrom, nmutation, pmutation, pcross, ncross):
    #initialise child variables
    child1 = []
    child2 = []

    #crossing site
    cross_pos = 0

    #randomly decide to cross
    if flip(pcross):
        ncross+=1
        cross_pos = random.randint(0,lchrom-1)
        ncross += 1
    else:
        cross_pos = lchrom - 1
    
    #now copy the parent's first half as it is to children
    try:
        for i in range(cross_pos):
            child1.append(parent1[i])
            child2.append(parent2[i])
        
        #now copy the changed parent's second half to children
        for i in range(cross_pos,lchrom):
            child1.append(parent2[i])
            child2.append(parent1[i])
        mutation(child1,pmutation,nmutation)
        mutation(child2,pmutation,nmutation)
        return [child1,child2]
    except Exception as e:
        print(e)
        return {"success":"false","message":"error producing offsprings"}