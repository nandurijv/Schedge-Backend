from flask import make_response

class main_process():
    def start_process(self):
        return make_response({"success":True, "message": "Processing End Point Reached"}, 200)