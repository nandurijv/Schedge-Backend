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
            token = str(request.headers.get('Authorization'))
            if re.match("^Bearer *([^ ]+) *$",token,flags=0):
                token = str(token.split(' ')[1])
                try:
                    key = str(os.getenv("SECRET_KEY"))
                    user = jwt.decode(token, key, algorithms = "HS256")
                    return func(*args)
                except Exception as e:
                    print(e)
                    return make_response({"success":False,"message":"Invalid Token"},400)
            else:
                return make_response({"success":False,"message":"Invalid Token"},400)
        return decorated_func  