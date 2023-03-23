from flask import jsonify, make_response, request
from schemas.tags_schema import TagSchema
from middlewares.pre_process import pre_process
from dotenv import load_dotenv
from geneticmodel.main import generation
import os
import json

pre_process_obj = pre_process()
load_dotenv()

class schedule_model():
    def get_schedule(self):

        return make_response({"success":True, "data": "Accessed get schedule endpoint"},200)
    
    def post_schedule(self, schedule):
        try:
            print("hi")
            print(schedule)
            data = generation(schedule)
            return make_response({"success":True, "data": data},200)
        except Exception as e:
            print(e)

