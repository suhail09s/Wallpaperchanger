import ctypes
import os
import threading
import random
import time
global wall
wall=[]
global path
global list
path='E:\Wallpapers\\'
t=0.5 # the duration in seconds
def listing(list,v):
    for a in range (len(list)):
        if str(list[a]).split('.')[-1]=='jpg' or str(list[a]).split('.')[-1]=='png':
            wall.append(v+'\\'+list[a])
list=os.listdir(path)

listing(list,"")
for v in list:
    try:    
        dirlist=os.listdir(path+v)
        listing(dirlist,v)
        print('found a folder',v)
    except:
        pass

 

ran=random.randint(0,len(wall))
path=path+'{}'
while True:
    time.sleep(t)
    ran=random.randint(0,len(wall))-1
    
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(path).format(wall[ran]) , 0)
    
