from schemas.tags_schema import TagSchema
import jwt
from flask import jsonify, make_response, request
from dotenv import load_dotenv
import json

load_dotenv()
class tag_model():
    def create_tags(self, tag):
        try:
            TagSchema(userID=tag["userID"],name=tag["name"],start_time=tag["start_time"],end_time=tag["end_time"]).save()
            tags = json.loads(TagSchema.objects(name=tag["name"])[0].to_json())
            return make_response({"success":True, "data": tags},200)
        except Exception as e:
            return make_response({"success":False, "data": e},400)     
