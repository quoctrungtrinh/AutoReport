# from asyncio import Event
# from timerThread import MyThread


# stopFlag = Event()
# thread = MyThread(stopFlag)
# thread.start()
# # this will stop the timer
# stopFlag.set()

import time
from downloadPaymentWix import WixCsv
from timerThread import RepeatTimer

wixCsv = WixCsv()

timer = RepeatTimer(1, wixCsv.test, args=(wixCsv,))
timer.start()

value = input("Please enter for stop:\n")

if value == '':
    timer.cancel()