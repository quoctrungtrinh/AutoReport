# from asyncio import Event
# from timerThread import MyThread


# stopFlag = Event()
# thread = MyThread(stopFlag)
# thread.start()
# # this will stop the timer
# stopFlag.set()

import time
from downloadOrderCsv import OrderCsv
from timerThread import RepeatTimer

ordercsv = OrderCsv()

timer = RepeatTimer(1, OrderCsv.Download, args=(ordercsv,'2022'))
timer.start()

value = input("Please enter for stop:\n")

if value == '':
    timer.cancel()