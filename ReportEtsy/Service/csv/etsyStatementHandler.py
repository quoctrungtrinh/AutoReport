import pandas
from Model.order import Order

class EtsyStatementHandler:           
    def Read(self, filePath):
        orders = []
        dfs = pandas.read_csv(filePath, parse_dates = ['Datum'])
        #for df in dfs:
            
        return orders
    

