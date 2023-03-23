import json
from geneticmodel.activity_fitness import activity_fitness

file = open('test.json')
data = json.load(file)

activities = data['activities']

def decode(chromosome):
    for i in range(len(chromosome)):
        #if no activity scheduled, do nothing
        if chromosome[i]==-1: chromosome[i]=0
        else:
            #get the activity object from the list
            a = activities[chromosome[i]]
            #now give this activity a fitness value based on its position at slot i
            chromosome[i] = activity_fitness(a,i)
    return chromosome
