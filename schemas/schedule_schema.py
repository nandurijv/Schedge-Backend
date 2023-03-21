from mongoengine import *
import datetime

class ScheduleSchema(Document):
    userid= ObjectIdField(required=True,unique=True)
    scheduleId = ObjectIdField(unique=True)
    meta = {"collection": "scheduleDb"}