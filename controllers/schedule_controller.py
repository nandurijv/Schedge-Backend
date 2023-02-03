from app import app, api
from models.schedule_model import schedule_model
from models.auth_model import auth_model
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

api.add_resource(GetSchedule,'/user/getSchedule', )

    