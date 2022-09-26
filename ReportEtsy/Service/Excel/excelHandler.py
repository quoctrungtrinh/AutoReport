from openpyxl import Workbook
from openpyxl import load_workbook
from Model.Constant import COLUMNS
import os
import shutil
import datetime

class ExcelHandler:
    def __init__(self, folderPath):
        self.FolderPath = folderPath
        self.ColNames = COLUMNS
        
    def ColNamesToOrderAtts(self):
        atts = []
        for col in self.ColNames:
            if col == 'Year':
                atts.append('Year')
            if col == 'Month':
                atts.append('Month')
            if col == 'Date':
                atts.append('Date')
            if col == 'Order ID':
                atts.append('OrderID')                
            if col == 'Transaction ID':
                atts.append('TransactionID')
            if col == 'Title':
                atts.append('Title')
            if col == 'Customer':
                atts.append('Kunden')
            if col == 'Address':
                atts.append('Address')
            if col == 'PLZ':
                atts.append('Plz')
            if col == 'City':
                atts.append('City')
            if col == 'Country':
                atts.append('Country')
            if col == 'Portal':
                atts.append('Portal')
        return atts

    def Create_Report(self,wsTitle,rows):
        date =  datetime.date.today().strftime('%d%m%Y')
        wb = Workbook()
        ws = wb.active

        ws.title = wsTitle
        ws.append(self.ColNames)

        for row in rows:
            ws.append(row)

        filePath = os.path.join(self.FolderPath, f'Bericht{date}.xlsx')

        wb.save(filePath)

    def Move_To_OneDrive(self,targetFolderPath):
        dest = shutil.move(self.FolderPath,targetFolderPath)



        

        

