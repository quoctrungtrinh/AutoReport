import inspect

class Order():
    def __init__(self):
        self.Year = ""
        self.Month = ""
        self.Date = ""
        self.OrderID = ""
        self.TransactionID = ""
        self.Title = ""
        self.Payment = ""
        self.TransactionFee = ""
        self.ProcessingFee = ""
        self.EinstellFee = ""
        self.Kunden = ""
        self.Address =""
        self.Plz = ""
        self.City = ""
        self.Country = ""
        self.Portal  = ""

    def ToRows(self,colNames):
        row = []
        for colName in colNames:
            row.append(self.__dict__[colName])

        return row



    # def GetMembers(self):
    #     members = []
    #     for i in inspect.getmembers(self):     
    #         #to remove private and protected functions
    #         if not i[0].startswith('_'):        
    #             # To remove other methods that
    #             # doesnot start with a underscore
    #             if not inspect.ismethod(i[1]): 
    #                 members.append(i[0])
    #     return members




