import random
import math
from geneticmodel.tag_slots import add_slots
from schemas.tags_schema import TagSchema
import json
def activity_fitness(activity, alloted_slot,data,userID):
    
    data2 = TagSchema.objects(userID=userID).to_json()
    slots = add_slots(data, json.loads(data2) )
    print("TAGS WITH ALLOWED SLOTS ARE: ",slots)
    print("Allocated slot is: ", alloted_slot)
    print("ACTIVITY TAGS: " , activity["tags"])
    tags = activity["tags"]
    fitness = 0
    print("INITIALLY TOTAL FITNESS IS: ",fitness)
    for i in range(len(tags)):
        for j in slots:
            print("COMPARING ",  j["_id"]["$oid"], "WITH", tags[i])
            if j["_id"]["$oid"]==tags[i]:
                for s in j["slots"]:
                    print("SLOT ALLOWED:", s)
                    if s==alloted_slot:
                        fitness+=2
                    elif abs(s-alloted_slot)<=1:
                        fitness+=1
                    elif abs(s-alloted_slot)>=3:
                        fitness-=2
                    else:
                        fitness-=1
                        
    return fitness
