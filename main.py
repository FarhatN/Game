# 🌳 🌊 🚁 ❎ 🔥 🏥 💗 🔋 🏦 ☁️ ⚡ 🥇

from map import Map
import time
import os

TICK_SLEEP = 0.05

tmp = Map(20, 10)
tmp.generate_forest(3, 10)
tmp.generate_river(10)
tmp.generate_river(10)
tmp.print_map()

tick = 1

while True:
    os.system('cls')
    print('TICK', tick)
    tmp.print_map()
    tick += 1
    time.sleep(TICK_SLEEP)