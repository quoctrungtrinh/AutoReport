from flask_restful import Resource
from flask import Response, request, jsonify
import os

class EtsyOrderFileController(Resource):
    def get(self):
        return Response((f"Orders"), status=200)
    
    def post(self):
        file = request.files['csv_file']
        fileName = file.filename
        
        if fileName.startswith("EtsySoldOrderItems2022") and fileName.endswith('.csv'):
            file.save(os.path.join('/Csv/','EtsySoldOrderItems2022.csv'))

        if fileName.startswith("EtsySoldOrderItems2021") and fileName.endswith('.csv'):
            file.save(os.path.join('/Csv/','EtsySoldOrderItems2021.csv'))

        if fileName.startswith("EtsySoldOrderItems2020") and fileName.endswith('.csv'):
            file.save(os.path.join('/Csv/','EtsySoldOrderItems2020.csv'))

        return Response((f"File updated successfully!"), status=200)