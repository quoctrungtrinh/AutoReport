# from watchdog.events import FileSystemEventHandler
# #import pyinotify


# class NewFileHandler(pyinotify.ProcessEvent):
#     # def on_created(self, event): # when file is created
#     #     # do something, eg. call your function to process the image
#     #     print(f"Got event for file {event.src_path}")

#     def process_IN_CLOSE_WRITE(self, event):                                    
#         """"                                                                    
#         Writtable file was closed.                                              
#         """                                                                                                    
#         print(f"write {event.pathname}")                                                

#     def process_IN_MOVED_TO(self, event):                                       
#         """                                                                     
#         File/dir was moved to Y in a watched dir (see IN_MOVE_FROM).            
#         """                                                                                                       
#         print(f"move {event.pathname}")                                                 

#     def process_IN_CREATE(self, event):                                         
#         """                                                                     
#         File/dir was created in watched directory.                              
#         """                 
#         fileName = event.pathname
                                                            
#         print(f"create {event.pathname}")                                                    
