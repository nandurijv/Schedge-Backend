from mongoengine import *
import datetime

class TagSchema(Document):
    userid= ObjectIdField(required=True,unique=True)
    # tags = ListField(DictField(required=True))
    name = StringField(required=True)
    start_time = StringField(required=True) 
    end_time = StringField(required=True)
    meta = {"collection": "tagsDb"}