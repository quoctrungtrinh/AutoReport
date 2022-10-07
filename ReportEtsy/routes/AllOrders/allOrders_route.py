from .controllers.allOrders import AllOrdersController
from .controllers.etsyOrders import EtsyOrdersController
from .controllers.wixOrders import WixOrdersController
from .controllers.etsyOrderFile import EtsyOrderFileController

class AllOrdersRoute:    
    def __init__(self, api):
        self.api = api
        
    def run(self):
        self.api.add_resource(AllOrdersController, '/allorders')
        self.api.add_resource(EtsyOrdersController,'/allorders/etsyorders')
        self.api.add_resource(EtsyOrderFileController,'/allorders/etsyorders/file')
        self.api.add_resource(WixOrdersController,'/allorders/wixorders')