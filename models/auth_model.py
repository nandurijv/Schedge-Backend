from flask import jsonify, request, make_response
from functools import wraps
from schemas.user_schema import UserSchema
import jwt
from dotenv import load_dotenv
import os
import re

load_dotenv()

class auth_model():
    def token_auth(self,func):
        @wraps(func)
        def decorated_func(*args):
            token = request.headers.get('Authorization')
            if re.match("^Bearer *([^ ]+) *$",token,flags=0):
                token = token.split(' ')[1]
                try:
                    user = jwt.decode(token,os.getenv(''), algorithms = "HS256")
                    request.headers.set('user',user)
                    return func(*args)
                except Exception as e:
                    return make_response({"success":False,"message":"Invalid Token"},400)
            else:
                return make_response({"success":False,"message":"Invalid Token"},400)
        return decorated_func  