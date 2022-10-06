from .controllers.allOrders import AllOrdersController

class AllOrdersRoute:    
    def __init__(self, api):
        self.api = api
        
    def run(self):
        self.api.add_resource(AllOrdersController, '/AllOrders')