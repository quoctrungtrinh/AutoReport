import datetime
from itertools import count
from types import CoroutineType
import pandas
from Model.Constant import EXCEL_PATH
from Model.order import Order
from Service.Excel.excelHandler import ExcelHandler
import sys
import time

class EtsyReportHandler:
    def __init__(self, fileOderPath):
        self.ordersDict = {}
        self.fileOderPath =  fileOderPath
        # self.fileStatementPath = fileStatementPath              
    
    def Proceed(self):        
        self.ReadFromEtsyOrderReport()
        self.MakeReport()
        

    def MakeReport(self):
        excelHandler = ExcelHandler(EXCEL_PATH)
        
        orders = list(self.ordersDict.values())
        rows = []
        for order in orders:
            row = order.ToRows(excelHandler.ColNamesToOrderAtts())
            rows.append(row)
        
        excelHandler.Create_Report("Kunden",rows)


    def ReadFromEtsyOrderReport(self):
        while (True):       
            try:        
                df = pandas.read_csv(self.fileOderPath)
                df['Verkaufsdatum'] = df['Verkaufsdatum'].astype('datetime64[ns]')

                for index, row in df.iterrows():
                    date = row['Verkaufsdatum']
                    title = row['Titel']
                    customer = row['Versandname']
                    address = row['Lieferadresse 1']
                    orderNr = row['Bestell-ID']
                    transactionID = row['Transaktions-Nr.']
                    plz = row['Versand-Postleitzahl']
                    city = row['Stadt des Versands']
                    country = row['Versandland']
                    portal = 'Etsy'

                    if (orderNr,transactionID) not in self.ordersDict:    
                        newKey = (orderNr,transactionID)
                        order = Order()
                        order.Date = date.date()
                        order.Month = date.month
                        order.Year = date.year
                        order.Title = title
                        order.OrderID = orderNr
                        order.TransactionID = transactionID
                        order.Kunden = customer
                        order.Address = address
                        order.Plz = plz
                        order.City = city
                        order.Country = country
                        order.Portal = portal
                        self.ordersDict[newKey] = order
                print('Finished reading order csv!')
                break                
            except PermissionError:
                time.sleep(1)
                #self.ReadFromEtsyOrderReport()
                #print(sys.exc_info()[0])
        
        


    

