from flask import jsonify, make_response, request
from schemas.user_schema import UserSchema
from middlewares.pre_process import pre_process
from dotenv import load_dotenv
from geneticmodel.main import generation
import os

pre_process_obj = pre_process()
load_dotenv()

class schedule_model():
    def get_schedule(self):

        return make_response({"success":True, "data": "Accessed get schedule endpoint"},200)
    
    def post_schedule(self, schedule):
        population = generation(schedule)
        return make_response({"success":True, "data": population},200)
        # return self.process_schedule()
