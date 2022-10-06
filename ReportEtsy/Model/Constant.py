import datetime
import os

COLUMNS = ['Year','Month','Date','Order ID','Transaction ID','Article ID','Title','Sale','Vendor','Personalized','Figure','Fulfillment Status','Customer','Address','PLZ','City','Country','Portal']

WATCH_PATH = r'C:\Users\z003cumd\Downloads'



date =  datetime.date.today().strftime('%d%m%Y')
EXCEL_FOLDERPATH = r'D:\EtsyTest'
EXCEL_FILEPATH = os.path.join(EXCEL_FOLDERPATH, f'Bericht_Stammdaten.xlsx')
EXCEL_WORKSHEET = "Kunden"