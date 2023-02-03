from mongoengine import *
import datetime

class ScheduleSchema(Document):
    
    meta = {"collection": "scheduleDb"}