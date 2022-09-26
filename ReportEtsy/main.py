#from Service.newFileHandler import NewFileHandler

# import pyinotify
from Model.Constant import WATCH_PATH
# from Service.newFileHandler import NewFileHandler
from Service.Etsy.downloadOrderCsv import OrderCsv
from Service.Etsy.downloadFinanceReport import FinanceReportCsv
from Service.csv.etsyStatementHandler import EtsyStatementHandler
from Service.csv.etsyReportHandler import EtsyReportHandler


import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil, os
import pathlib
  
  
class OnMyWatch:
    # Set the directory on watch
    watchDirectory = WATCH_PATH
  
    def __init__(self):
        self.observer = Observer()
  
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
  
        self.observer.join()
  
  
class Handler(FileSystemEventHandler):
  
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
  
        elif event.event_type == 'created':
            print(event)
            # Event is created, you can process it now
            filePath = pathlib.PureWindowsPath(rf'{event.src_path}').as_posix()
            etsyReportHandler = EtsyReportHandler(filePath)
            result = etsyReportHandler.Proceed()
            print(result)
            

              
  
if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()



