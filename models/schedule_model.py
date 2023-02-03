from flask import jsonify, make_response, request
from schemas.user_schema import UserSchema
from app import flask_bcrypt, mail
import jwt
from flask_mail import Message
from dotenv import load_dotenv
import os

load_dotenv()

class schedule_model():
    def get_schedule(self):
        return make_response({"success":True, "data": "Accessed schedule endpoint"},200)