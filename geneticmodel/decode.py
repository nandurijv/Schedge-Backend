import json
from geneticmodel.activity_fitness import activity_fitness

def decode(chromosome, data,userID):
    for i in range(len(chromosome)):
        #if no activity scheduled, do nothing
        if chromosome[i]==-1: chromosome[i]=0
        else:
            #get the activity object from the list
            a = data["activities"][chromosome[i]]
            #now give this activity a fitness value based on its position at slot i
            chromosome[i] = activity_fitness(a,i,data,userID)
    return chromosome
