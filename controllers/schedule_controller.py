from app import app, api
from models.schedule_model import schedule_model
from middlewares.auth_model import auth_model
from flask_restful import Resource, Api, reqparse
from flask import make_response
from mongoengine import *
import os
import jwt
obj = schedule_model()
auth = auth_model()

parser = reqparse.RequestParser()
parser.add_argument('interval_start',type=str,help="Please provide tag name")
parser.add_argument('interval_end',type=str,help="Please provide start_time")
parser.add_argument('slot_dur',type=str,help="Please provide end_time")
parser.add_argument('activities',type=list,location="json",help="Please provide activity list")

class GetSchedule(Resource):
    method_decorators = {"get":[auth.token_auth]}
    def get(self):
        return obj.get_schedule()

class PostSchedule(Resource):
    method_decorators = {"post":[auth.token_auth]}
    def post(self):
        schedule = parser.parse_args()
        return obj.post_schedule(schedule)


api.add_resource(GetSchedule,'/user/getSchedule', )
api.add_resource(PostSchedule,'/user/postSchedule',)