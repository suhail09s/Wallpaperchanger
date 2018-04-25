import time
import keyboard
import ctypes
import os
import threading
import random
import glob
global wall
import winsound
global path
start=True
global counter
walllist=[]
counter=10
path='e:\Wallpapers\\' # the path has to end with  (\\)


def main():
    
    
    starttime=time.time()
    try:
        wall=readdir(path)
        print ('Looping through:',len(wall),'wallpapers')
    except:
        print ('ERROR: Failed to read wallpapers directory')
        exit()
    ran=random.randint(0,len(wall))

    print ('All wallpapers were loaded in',(time.time()-starttime),'secounds')
    if len(wall)==0:
        print('No wallpapers were found, please check path.')      
        exit(0)
    return wall


def readdir(path):
    counter=0 
    for filename in glob.iglob(path + '**/*.***', recursive=True):
        counter+=1
        if str(filename).split('.')[-1]=='jpg' or str(filename).split('.')[-1]=='png' or str(filename).split('.')[-1]=='gif':
            walllist.append(filename)
                
        if counter %10000 ==0: # msg when the script takes too long and looks frozen
            print('still reading, reached:',filename)
    return walllist


def checker(start,counter):
     global starter
     if start==True:
        start=script(counter)
        
        return start
     else:
        pass
		

def changer():
    ran=random.randint(0,len(wall))-1
    ctypes.windll.user32.SystemParametersInfoW(20, 0,str(wall[ran]) , 0)
    print (wall[ran])
	
	
def script(counter):
    while True:
     if counter==0:
        changer()
        return True
     else:
        print(counter)
        counter-=1
        time.sleep(1)
        if keyboard.is_pressed('shift+ctrl+s'):
            return True
            

        if keyboard.is_pressed('shift+ctrl+a'):  
            print('Paused')
            duration = 500  # millisecond
            freq = 400 # Hz
            winsound.Beep(freq, duration)
            return False

			
        ##################################################
print('Keep holding Space+ctrl+A for 1 second or till you hear a beep to pause/resume the script,\nyou can jump to the next wallpaper by holding shift+ctrl+s for 1 second')
wall=main()
#counter=int(input('Enter an integer number in secounds how fast looping through wallpapers:')) ask for timer value from user(Turned off feature)
while True:
    try:
        start=checker(start,counter)
    except:
        print('ERROR:Failed to read timer.')
        exit()
    time.sleep(1)
    if keyboard.is_pressed('shift+ctrl+a'):
        start=True
        print('resumed')
        duration = 500  # millisecond
        freq = 500 # Hz
        winsound.Beep(freq, duration)
    if keyboard.is_pressed('shift+ctrl+s'):
        changer()
        duration = 500  # millisecond
        freq = 500 # Hz
        winsound.Beep(freq, duration)
        print ('NEXT!!')
        