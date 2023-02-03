from flask import jsonify, make_response, request
from schemas.user_schema import UserSchema
from middlewares.pre_process import pre_process
from dotenv import load_dotenv
import os

pre_process_obj = pre_process()
load_dotenv()

class schedule_model():
    def get_schedule(self):
        return make_response({"success":True, "data": "Accessed get schedule endpoint"},200)
    
    def post_schedule(self):
        # return make_response({"success":True, "data": "Accessed post schedule endpoint"},200)
        return self.process_schedule()
    
    def process_schedule(self):
        return pre_process_obj.pre_process({"schedule": "schedule_name"})