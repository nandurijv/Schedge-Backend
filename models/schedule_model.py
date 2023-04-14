from flask import jsonify, make_response, request
from dotenv import load_dotenv
from geneticmodel.main import generation
load_dotenv()

class schedule_model():
    def get_schedule(self):
        
        return make_response({"success":True, "data": "Accessed get schedule endpoint"},200)
    
    def post_schedule(self, schedule):
        try:
            print(schedule)
            data = generation(schedule)
            return make_response({"success":True, "data": data},200)
        except Exception as e:
            print(e)
            return make_response({"success":"false","message":"Error Generating Schedule"},400)

