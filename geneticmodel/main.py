import json
from geneticmodel.initialise import initialise
from geneticmodel.selection import roulette_wheel_selection
from geneticmodel.fitness import fitness
from geneticmodel.crossover import crossover
from geneticmodel.average_fitness import average_fitness

#define constants
pop_size = 15
num_gen = 1000
num_parents = 2
n_mutation = 0 #number of mutations
p_mutation = 0.001 #probability of mutation
p_cross = 1 #that is every parent must cross
n_cross = 0 #number of crosses

def generation(data):
    #store the list in a variable
    list_of_activities = data['activities']
    len_act = len(list_of_activities)

    #the duration of intervals
    lchrom = int((data["interval_end"]-data["interval_start"])/data["slot_dur"])
    curr_gen = 0
    #average fitness of the population
    avg_fitness = []
    max_fit = []
    gen_list= []
    # initialise a population
    population = initialise(pop_size, lchrom, len_act)
    while curr_gen!=num_gen:
        curr_gen += 1
        #select individuals for mating
        parents = roulette_wheel_selection(population, fitness, num_parents)
        #perform crossover
        children = crossover(population[parents[0]],population[parents[1]],lchrom,n_mutation,p_mutation,p_cross,n_cross)
        
        #update the population
        
        population.append(children[0])
        population.append(children[1])
        
        # add to the fitness of the population
        stats = average_fitness(population)
        avg_fitness.append(stats[0])
        max_fit.append(stats[1])
        gen_list.append(curr_gen)
    return population
