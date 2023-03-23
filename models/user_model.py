from flask import jsonify
from schemas.user_schema import UserSchema
from app import flask_bcrypt, mail
import jwt
from flask_mail import Message
from dotenv import load_dotenv
import os

load_dotenv()
class user_model():

    def mail_user(self, user):
        user = UserSchema.objects(email=user["email"])[0]
        encoded_jwt = jwt.encode({"email":user["email"]},os.getenv("SECRET_KEY"),algorithm="HS256")
            # return {"success":False, "message":"Internal Error Occurred"}

        msg = Message("Hello", sender=os.getenv("SENDER_MAIL"),recipients=[user["email"]])
        msg.html = "<h1>Welcome to Schedge!</h1> <p>Testing Phase. Verify your email address by clicking this <a href='{}' target='_blank'>link</a>.</p>".format(os.getenv("BASE_URL")+"/user/verifyUser/"+encoded_jwt)
        try:
            mail.send(msg)
        except Exception as err:
            return {"success":False, "message":"Internal Error Occurred"}
        return {"success":True, "message":"Verification Mail Sent!"}

    def create_user(self, userModel):
        user = UserSchema.objects(email=userModel["email"])
        if len(user) != 0:
            return {"success":False, "message":"User Already Exists"}
        else:

            UserSchema(name=userModel["name"],email=userModel["email"],password=flask_bcrypt.generate_password_hash(userModel["password"], 12)).save()
            res = self.mail_user(userModel)
            message= ""
            if res["success"]:
                message = "Created User Successfully. Verify Your Email."
            else:
                message = res["message"]
            return {"success":res["success"], "message":message}
   
    def verify_email(self, token):
        try:
            user_email = jwt.decode(token, os.getenv("SECRET_KEY"),algorithms=["HS256"])
        except Exception as err:
            return {"success":False, "message": "Invalid Token"}
        print(user_email)
        user = UserSchema.objects(email=user_email["email"])
        if len(user) == 0:
            return {"success":False, "message":"Verification Unsuccessful"}
        else:
            user.update(verified=True)
            return {"success":True, "message":"Verification Successful!"}

    def login_user(self, user):
        find_user = UserSchema.objects(email=user["email"])[0]
        if len(find_user) == 0:
            return {"success":False, "message":"No Such User Exists"}
        else:
            if find_user["verified"] == True:
                userID = str(find_user["id"])
                print(userID)
                try:
                    encoded_user = jwt.encode({"user": user["email"]},os.getenv("SECRET_KEY"),algorithm="HS256")
                    return {"success":True, "message":"User Logged In Successfully","token":encoded_user, "userID":userID, "name": find_user["name"], "email": find_user["email"]}
                except Exception as err:
                    print(err)
                    return {"success":False, "message":"Internal Error Occurred"},500
            else:
                return {"success":False, "message":"User Not Verified"}
        return jsonify(user)