import ctypes
import os
import threading
import random
import time
import win32file
global wall
wall=[]
global path
global list
path='c:\\' # the path has to end with  (\\)
t=5           # the duration in seconds
def listing(list,v):
    for a in range (len(list)):
        if str(list[a]).split('.')[-1]=='jpg' or str(list[a]).split('.')[-1]=='png' or str(list[a]).split('.')[-1]=='gif':
            wall.append(v+'\\'+list[a])
start=time.time()
list=os.listdir(path)

listing(list,"")
for v in list:
    try:    
        dirlist=os.listdir(path+v)
        listing(dirlist,v)
        print('found a folder',v)
    except:
        pass

print (len(wall),'Wallpapers were found')
ran=random.randint(0,len(wall))
path=path+'{}'
print (time.time()-start)
if len(wall)==0:
    print('No wallpapers were found, please check.')
    exit(0)

while True:
    time.sleep(t)
    ran=random.randint(0,len(wall))-1
    
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(path).format(wall[ran]) , 0)
    
