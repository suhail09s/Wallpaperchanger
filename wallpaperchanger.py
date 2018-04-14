import ctypes
import os
import threading
import random
import time

list=os.listdir("e:\Wallpapers")
wall=[]
for a in range (len(list)):
    if str(list[a]).split('.')[-1]=='jpg' or str(list[a]).split('.')[-1]=='png':
        wall.append(list[a])
print (wall)
ran=random.randint(0,len(wall))
while True:
    time.sleep(5)
    ran=random.randint(0,len(wall))
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "E:\Wallpapers\{}".format(wall[ran]) , 0)
