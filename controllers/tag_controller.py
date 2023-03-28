from app import app, api
from models.tag_model import tag_model
from middlewares.auth_model import auth_model
from flask_restful import Resource, Api, reqparse
from flask import make_response,request
from app import app
import os
import jwt
obj = tag_model()
auth = auth_model()

parser = reqparse.RequestParser()
parser.add_argument('userID',type=str,help="Please provide userID")
parser.add_argument('name',type=str,help="Please provide tag name")
parser.add_argument('start_time',type=str,help="Please provide start_time")
parser.add_argument('end_time',type=str,help="Please provide end_time")

class createTags(Resource):
    method_decorators = {"post":[auth.token_auth]}
    def post(self):
        tag = parser.parse_args()
        return obj.create_tags(tag)

class updateTags(Resource):
    method_decorators = {"put":[auth.token_auth]}
    def put(self):
        tag = parser.parse_args()
        return obj.update_tag(tag)

class getTags(Resource):
    method_decorators = {"get":[auth.token_auth]}
    def get(self):
        userID = request.args.get('userID')
        return obj.get_tags(userID)


api.add_resource(createTags,'/user/createTag', )
api.add_resource(updateTags,'/user/putTag', )
api.add_resource(getTags,'/user/getTags',)