from schemas.tags_schema import TagsSchema
import jwt
from flask import jsonify, make_response, request
from dotenv import load_dotenv

load_dotenv()
class tag_model():
    def create_tags(self, tagsModel):
        return make_response({"success":True, "data": "Accessed get schedule endpoint"},200)

