from flask_restful import Resource
from flask import Response,send_file

class AllOrdersController(Resource):
    def get(self):
        path = "/Excel/Bericht_Stammdaten.xlsx"
        return send_file(path, as_attachment=True)