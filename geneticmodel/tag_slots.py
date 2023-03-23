import json
import math
file = open('test.json')
data = json.load(file)
start = data["interval_start"]
end = data["interval_end"]

slot_dur = data["slot_dur"]

file2 = open("tags.json")
data2 = json.load(file2)

def add_slots():
    tags = data2["tags"]
    for i in tags:
        i["slots"] = [math.ceil(i/slot_dur) for i in range(i['start_time']-start, i['end_time']-start,slot_dur)]
    return tags

slots = add_slots()