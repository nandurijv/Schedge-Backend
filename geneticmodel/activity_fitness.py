import random
import math
from geneticmodel.tag_slots import slots
def activity_fitness(activity, alloted_slot):
    tags = activity["tags"]
    fitness = 0
    for i in range(len(tags)):
        if alloted_slot in slots[tags[i]-1]["slots"]:
            fitness+=1
    return fitness
