from app import app, api
from models.schedule_model import schedule_model
from middlewares.auth_model import auth_model
from flask_restful import Resource, Api, reqparse
from flask import make_response
import os
import jwt
obj = schedule_model()
auth = auth_model()

class GetSchedule(Resource):
    method_decorators = {"get":[auth.token_auth]}
    def get(self):
        return obj.get_schedule()

class PostSchedule(Resource):
    method_decorators = {"post":[auth.token_auth]}
    def post(self):
        return obj.post_schedule()


api.add_resource(GetSchedule,'/user/getSchedule', )
api.add_resource(PostSchedule,'/user/postSchedule',)