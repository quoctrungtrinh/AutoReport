import datetime
from itertools import count
from types import CoroutineType
import pandas
from Model.order import Order
from Model.book import Book
from Model.Constant import EXCEL_WORKSHEET
from Service.Excel.excelHandler import ExcelHandler
import sys
import time


class EtsyReportHandler:
    def __init__(self, fileOderPath):
        self.ordersList = []
        self.fileOderPath =  fileOderPath
        # self.fileStatementPath = fileStatementPath              
    
    def ProceedAndMake(self):        
        self.ReadFromEtsyOrderReport()
        self.MakeReport()

    def ProceedAndAppend(self):
        self.ReadFromEtsyOrderReport()
        self.AppendReport()        

    def MakeReport(self):
        excelHandler = ExcelHandler()
        rows = []
        for order in self.ordersList:
            row = order.ToRows(excelHandler.ColNamesToOrderAtts())
            rows.append(row)
        
        excelHandler.Create_Report(EXCEL_WORKSHEET,rows)

    def AppendReport(self):
        excelHandler = ExcelHandler()
        rows = []
        for order in self.ordersList:
            row = order.ToRows(excelHandler.ColNamesToOrderAtts())
            rows.append(row)
        
        excelHandler.Append_Report(EXCEL_WORKSHEET,rows)
        print("Update report finished!")

    def ReadFromEtsyOrderReport(self):      
        try:        
            df = pandas.read_csv(self.fileOderPath)
            df['Verkaufsdatum'] = df['Verkaufsdatum'].astype('datetime64[ns]')

            for index, row in df.iterrows():                
                articleID = row['Artikel-ID']
                date = row['Verkaufsdatum']
                title = row['Titel']
                customer = row['Versandname']
                address = row['Lieferadresse 1']
                orderNr = row['Bestell-ID']
                transactionID = row['Transaktions-Nr.']
                plz = row['Versand-Postleitzahl']
                city = row['Stadt des Versands']
                country = row['Versandland']
                fulfillmentStt = ""
                isPersonalized = ""
                figure = ""
                quantity = int(row['Stückzahl'])
                portal = 'Etsy'
                sale = row['Gesamtanzahl Artikel']
                

                
                order = Order()
                order.ArticleID = str(articleID)
                book = Book(str(articleID))
                book.GetInfo()            
                order.Date = str(date.strftime('%d.%m.%Y'))
                order.Month = date.month
                order.Year = date.year
                order.Title = book.GerShortName
                order.Key = order.Year + order.Month + order.Title
                order.Vendor = book.Vendor
                order.OrderID = str(orderNr)
                order.TransactionID = str(transactionID)
                order.Kunden = customer
                order.Address = address
                order.Plz = plz
                order.City = city
                order.Country = country
                order.Sale = sale
                order.isPersonalized = isPersonalized
                order.Figure = figure
                order.FulfillmentStt = fulfillmentStt
                order.Portal = portal
                for i in range(quantity):
                    self.ordersList.append(order)
            print('Finished reading order csv!')
            return                
        except PermissionError:
            self.ReadFromEtsyOrderReport()
            #print(sys.exc_info()[0])
        
        


    

