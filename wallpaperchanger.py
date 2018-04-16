import ctypes
import os
import threading
import random
import time
import glob
global wall
walllist=[]
global path
def readdir(path):
            counter=0 
            for filename in glob.iglob(path + '**/*.***', recursive=True):
             counter+=1
             if str(filename).split('.')[-1]=='jpg' or str(filename).split('.')[-1]=='png' or str(filename).split('.')[-1]=='gif':
                walllist.append(filename)
                
             if counter %1000 ==0: # msg when the script takes too long and looks frozen
                 print('still reading, reached:',filename)
            return walllist
path='e:\Wallpapers\\' # the path has to end with  (\\)
t=10          # the duration in seconds
start=time.time()
wall=readdir(path)
print ('Looping through:',len(wall),'wallpapers')

ran=random.randint(0,len(wall))

print (time.time()-start)
if len(wall)==0:
    print('No wallpapers were found, please check path.')
    exit(0)

while True:
    time.sleep(t)
    ran=random.randint(0,len(wall))-1
    
    ctypes.windll.user32.SystemParametersInfoW(20, 0,str(wall[ran]) , 0)
    print (wall[ran])
    
