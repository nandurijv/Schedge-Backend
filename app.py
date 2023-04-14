from flask import Flask
from flask_restful import Resource, Api, reqparse
from mongoengine import connect
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = os.getenv("SENDER_MAIL"),
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
))

flask_bcrypt = Bcrypt(app)
mail = Mail(app)
mail.init_app(app)

print("CONNECTED TO THE SERVER", (connect(host="mongodb+srv://admin:Na%40081202@cluster0.zv0im.mongodb.net/?retryWrites=true&w=majority").server_info()['ok']))

@app.route('/')
@cross_origin()
def welcome():
    return "Server is Running ..."

from controllers import *

if __name__ == "__main__":
    app.run(debug=True)
    print("APP LISTENING ON PORT 5000")
