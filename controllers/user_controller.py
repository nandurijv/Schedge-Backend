from app import app, api
from models.user_model import user_model
from flask_restful import Resource, Api, reqparse, request
obj = user_model()

parser = reqparse.RequestParser()
parser.add_argument('name',type=str,help="Please provide your full name")
parser.add_argument('email',type=str,help="Please provide your email address")
parser.add_argument('password',type=str,help="Please provide your password")

login_parser = reqparse.RequestParser()
login_parser.add_argument('email',type=str,help="Please provide your email address")
login_parser.add_argument('password',type=str,help="Please provide your password")

class CreateUser(Resource):
    def post(self):
        user = parser.parse_args()
        return obj.create_user(user)
        # return {"data":"this is a get request to user signup"}, 200

class VerifyUser(Resource):
    def get(self,token):
        return obj.verify_email(token)
        # return {"data":"this is a get request to user signup"}, 200

class LoginUser(Resource):
    def post(self):
        user = login_parser.parse_args()
        return obj.login_user(user)
        # return {"data":"this is a get request to user signup"}, 200

class ResendMail(Resource):
    def post(self):
        user = parser.parse_args()
        return obj.mail_user(user)


api.add_resource(CreateUser,'/user/createUser')
api.add_resource(VerifyUser,'/user/verifyUser/<string:token>')
api.add_resource(LoginUser,'/user/loginUser')
api.add_resource(ResendMail,'/user/resendMail')