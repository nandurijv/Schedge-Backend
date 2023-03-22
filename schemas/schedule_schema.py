from mongoengine import *
import datetime

class ScheduleSchema(Document):
    userid= ObjectIdField(required=True,unique=True)
    scheduleId = StringField(unique=True)
    interval_start = StringField(required=True)
    interval_end = StringField(required=True)
    slot_dur = StringField(required=True)
    activities = DictField(required=True)
    meta = {"collection": "scheduleDb"}