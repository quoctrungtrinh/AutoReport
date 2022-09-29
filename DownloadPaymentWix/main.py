# from asyncio import Event
# from timerThread import MyThread


# stopFlag = Event()
# thread = MyThread(stopFlag)
# thread.start()
# # this will stop the timer
# stopFlag.set()

import requests
import json

url = "http://hannas1stbooks.com/_functions/getOrders"

payload = json.dumps({
  "user": "quoctrungtrinh@live.com",
  "password": "Zorro283!"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

resjson = json.loads(response.text)
print(resjson[0])
#print(lengthresjson)
# orders = response.text
# print(orders)

