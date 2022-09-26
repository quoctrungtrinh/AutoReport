from threading import Timer

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


# class MyThread(Thread):
#     def __init__(self, event):
#         Thread.__init__(self)
#         self.stopped = event

#     def run(self):
#         while not self.stopped.wait(0.5):
#             print("my thread")
#             # call a function