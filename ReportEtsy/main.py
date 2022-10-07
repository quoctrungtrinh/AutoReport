

# from Service.Etsy.downloadOrderCsv import OrderCsv
# from Service.Etsy.downloadFinanceReport import FinanceReportCsv
# from Service.csv.etsyStatementHandler import EtsyStatementHandler
# from Service.csv.etsyReportHandler import EtsyReportHandler

from flask import Flask
from flask_restful import Api

# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import shutil, os
# import pathlib
  
  
# class OnMyWatch:
#     # Set the directory on watch
#     watchDirectory = WATCH_PATH
  
#     def __init__(self):
#         self.observer = Observer()
  
#     def run(self):
#         event_handler = Handler()
#         self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
#         self.observer.start()
#         try:
#             while True:
#                 time.sleep(5)
#         except:
#             self.observer.stop()
#             print("Observer Stopped")
  
#         self.observer.join()
  
  
# class Handler(FileSystemEventHandler):
  
#     @staticmethod
#     def on_any_event(event):
#         if event.is_directory:
#             return None
  
#         elif event.event_type == 'created':
#             filePath = pathlib.PureWindowsPath(rf'{event.src_path}').as_posix()
#             fileName = os.path.basename(filePath)
#             print(f"{fileName} was downloaded!")
#             # Event is created, you can process it now
#             if fileName.startswith("EtsySoldOrderItems2022") and filePath.endswith(".csv"):
#                 etsyReportHandler = EtsyReportHandler(filePath)
#                 etsyReportHandler.Proceed()
#                 wixOrderHandler = WixOrderHandler()
#                 wixOrderHandler.Proceed()
                
# class Reporter():
#     def make(self):
#         filePath2020 = r'D:\Projects\Private\AutoReport\AutoReport\ReportEtsy\Csv\EtsySoldOrderItems2020.csv'
#         filePath2021 = r'D:\Projects\Private\AutoReport\AutoReport\ReportEtsy\Csv\EtsySoldOrderItems2021.csv'
#         filePath2022 = r'D:\Projects\Private\AutoReport\AutoReport\ReportEtsy\Csv\EtsySoldOrderItems2022.csv'

#         etsyReportHandler = EtsyReportHandler(filePath2020)
#         etsyReportHandler.ProceedAndMake()
#         etsyReportHandler = EtsyReportHandler(filePath2021)
#         etsyReportHandler.ProceedAndAppend()
#         etsyReportHandler = EtsyReportHandler(filePath2022)
#         etsyReportHandler.ProceedAndAppend()
#         wixOrderHandler = WixOrderHandler()
#         wixOrderHandler.Proceed()
            

server = Flask(__name__)
api = Api(server)          

from routes.AllOrders.allOrders_route import AllOrdersRoute
AllOrdersRoute(api).run()


if __name__ == '__main__':
    # watch = OnMyWatch()
    # watch.run()
    #reporter = Reporter()
    #reporter.make()
    #192.168.178.96
    server.run(host='0.0.0.0', port='8080')




