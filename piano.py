from ppadb.client import Client
import numpy as np
from mss import mss
import time
adb  = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print("no device connected")
    quit()

device = devices[0]


col1 = {'left': 50,  'top':600, 'width': 1, 'height': 1}
col2 = {'left': 150, 'top':600, 'width': 1, 'height': 1}
col3 = {'left': 250, 'top':600, 'width': 1, 'height': 1}
col4 = {'left': 350, 'top':600, 'width': 1, 'height': 1}

sct = mss()

col_1 = False
col_2 = False
col_3 = False
col_4 = False

while True:

    col1_pixel = np.array(sct.grab(col1))
    col2_pixel = np.array(sct.grab(col2))
    col3_pixel = np.array(sct.grab(col3))
    col4_pixel = np.array(sct.grab(col4))

    col1_b = sum(col1_pixel[0][0][:2])
    col2_b = sum(col2_pixel[0][0][:2])
    col3_b = sum(col3_pixel[0][0][:2])
    col4_b = sum(col4_pixel[0][0][:2])
    # print(col1_b, col2_b, col3_b, col4_b)

    if col1_b<30 and not col_1:
        print("col 1")
        device.shell('input tap 184 2040')
        col_1 = True
        col_2 = False
        col_3 = False
        col_4 = False
        continue
    if col2_b<30  and not col_2:
        print("col 2")
        device.shell('input tap 406 2040')
        col_1 = False
        col_2 = True
        col_3 = False
        col_4 = False
        continue
    if col3_b<30  and not col_3:
        print("col 3")
        device.shell('input tap 670 2040')
        col_2 = False
        col_1 = False
        col_3 = True
        col_4 = False
        continue
    if col4_b<30 and not col_4:
        print("col 4")
        device.shell('input tap 919 2040')
        col_2 = False
        col_3 = False
        col_1 = False
        col_4 = True
        continue

