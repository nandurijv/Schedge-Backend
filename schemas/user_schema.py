from mongoengine import *
import datetime

class UserSchema(Document):
    name = StringField(max_length=200,required=True)
    email = StringField(max_length=200,required=True,unique=True)
    password = StringField(min_length=8,required=True)
    verified = BooleanField(default=False)
    date_created = DateTimeField(default=datetime.datetime.utcnow)
    meta = {"collection": "userDb"}