from flask_restful import Resource
from flask import Response
from os import listdir
from os.path import isfile, join
import os

from Service.csv.etsyReportHandler import EtsyReportHandler

class EtsyOrdersController(Resource):
    def get(self):
        return Response((f"Orders"), status=200)

    def post(self):
        count = 0
        onlyfiles = [f for f in listdir('/Csv/') if isfile(join('/Csv/', f))]
        for file in onlyfiles:
            count += 1
            filePath = os.path.join('/Csv/',file)
            print(f'filePath = {filePath}')
            etsyReportHandler = EtsyReportHandler(filePath)
            if count == 1:
                etsyReportHandler.ProceedAndMake()
            if count > 1:
                etsyReportHandler.ProceedAndAppend()
        return Response((f"Finished Etsy Orders"), status=200)