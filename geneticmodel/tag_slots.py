import json
import math
from schemas.tags_schema import TagSchema

def add_slots(data, data2):
    
    slot_dur = int(data["slot_dur"])
    start = int(data["interval_start"])

    tags = data2
    
    for i in range(len(tags)):
        tags[i]["slots"] = [math.ceil(j/slot_dur) for j in range(int(tags[i]['start_time'])-start, int(tags[i]['end_time'])-start,slot_dur)]
    print("tags are: ",data2)
    print()
    return tags