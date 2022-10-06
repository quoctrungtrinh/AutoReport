from flask_restful import Resource
from flask import Response

class AllOrdersController(Resource):
    def get(self):
        return Response((f"Orders"), status=200)