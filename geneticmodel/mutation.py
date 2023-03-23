from geneticmodel.flip import biased_coin_flip as flip
import random
def mutation(chromosome,pmutation,nmutation):
    if flip(pmutation):
        nmutation+=1
        available_indices = [i for i in range(len(chromosome)) if chromosome[i]==-1]
        if len(available_indices)==0:
            available_indices.append(len(chromosome)-1)
        swap_empty_index = random.choice(available_indices)
        #randomly chose from these indices and exchange with the randomly chosen other index
        activity_indices = [i for i in range(len(chromosome)) if chromosome[i]!=-1]
        if len(activity_indices)==0:
            activity_indices.append(0)
        swap_activity_index = random.choice(activity_indices)
        temp = chromosome[swap_activity_index]
        chromosome[swap_activity_index] = chromosome[swap_empty_index]
        chromosome[swap_empty_index] = temp
        return chromosome
    else:
        return chromosome