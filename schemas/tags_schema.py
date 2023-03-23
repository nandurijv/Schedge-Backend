from mongoengine import *
import datetime

class TagSchema(Document):
    userID= ObjectIdField(required=True, unique=False)
    name = StringField(required=True,unique=True)
    start_time = StringField(required=True) 
    end_time = StringField(required=True)
    meta = {"collection": "tagsDb"}