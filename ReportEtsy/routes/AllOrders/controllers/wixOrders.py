from flask_restful import Resource
from flask import Response
from Service.Wix.wixOrderHandler import WixOrderHandler
class WixOrdersController(Resource):
    def post(self):
        wixOrderHandler = WixOrderHandler()
        wixOrderHandler.Proceed()
        return Response((f"Finished Wix Orders"), status=200)