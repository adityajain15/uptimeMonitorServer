#!/usr/bin/env python
import asyncio
import datetime
import random
import websockets
import psutil
import os

async def time(websocket, path):
  while True:
    one_min_average = os.getloadavg()[0]
    num_cores = psutil.cpu_count()
    normalised_load = str(one_min_average / num_cores)
    await websocket.send(normalised_load)
    await asyncio.sleep(10)

start_server = websockets.serve(time, '127.0.0.1', 8888)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()