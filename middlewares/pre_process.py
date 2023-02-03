from flask import make_response
from middlewares.main_process import main_process
import pygad

main = main_process()

class pre_process():
    def pre_process(self, schedule):
        return main_process.start_process(self)