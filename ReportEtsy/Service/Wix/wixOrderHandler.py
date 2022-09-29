import requests
import json
from datetime import datetime
from Model.order import Order
from Model.book import Book
from Model.Constant import EXCEL_WORKSHEET
from Service.Excel.excelHandler import ExcelHandler

class WixOrderHandler:
    def __init__(self):
        self.ordersList = []

    def Proceed(self):
        self.GetOrders()
        self.UpdateReport()

    def GetOrders(self):
        url = "http://hannas1stbooks.com/_functions/getOrders"

        payload = json.dumps({
        "user": "quoctrungtrinh@live.com",
        "password": "Zorro283!"
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        wixOrders = json.loads(response.text)
        

        for wixOrder in wixOrders:
                lineItems = wixOrder['lineItems']
                
                date = datetime.strptime(wixOrder['_dateCreated'][0:10], '%Y-%m-%d') 
                # title = wixOrder['Titel']
                customer = wixOrder['shippingInfo']['shipmentDetails']['firstName'] + " " + wixOrder['shippingInfo']['shipmentDetails']['lastName']
                address = wixOrder['shippingInfo']['shipmentDetails']['address']['addressLine']
                orderNr = wixOrder['number']
                transactionID = wixOrder['billingInfo']["paymentProviderTransactionId"]
                plz = wixOrder['shippingInfo']['shipmentDetails']['address']['postalCode']
                city = wixOrder['shippingInfo']['shipmentDetails']['address']['city']
                country = wixOrder['shippingInfo']['shipmentDetails']['address']['country']
                fulfillmentStt = wixOrder['fulfillmentStatus']
                figure = ' '
                isPersonalized = ' '
                portal = 'Wix'

                for item in lineItems:
                    articleID = item['productId']
                    if len(item['options']) > 0:
                        isPersonalized =  'Yes' if item['options'][0]['selection'] == 'Mit Personalisierung' else 'No'
                    if len(item['options']) > 1:
                        figure = item['options'][1]['selection']
                    
                    newKey = (orderNr,articleID)
                    order = Order()
                    order.ArticleID = str(articleID)
                    book = Book(str(articleID))
                    book.GetInfo()            
                    order.Date = date.strftime('%d.%m.%Y')
                    order.Month = date.month
                    order.Year = date.year
                    order.Title = book.GerShortName
                    order.FulfillmentStt = fulfillmentStt
                    order.isPersonalized = isPersonalized
                    order.Figure = figure
                    order.OrderID = str(orderNr)
                    order.TransactionID = str(transactionID)
                    order.Kunden = customer
                    order.Address = address
                    order.Plz = plz
                    order.City = city
                    order.Country = country
                    order.Portal = portal
                    self.ordersList.append(order)

        print('Finished getting orders from wix!')
    
    def UpdateReport(self):
        excelHandler = ExcelHandler()
        rows = []
        for order in self.ordersList:
            row = order.ToRows(excelHandler.ColNamesToOrderAtts())
            rows.append(row)
        
        excelHandler.Append_Report(EXCEL_WORKSHEET,rows)
        print("Update report finished!")
        
            