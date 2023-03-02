import os
import threading
import cv2
import modules

inputFile = "test-footage/test_Trim.mp4"
scale = 4
length = modules.vidLen(inputFile)

threads = 5
n = 0
while n<length+1:
    if threading.active_count()<threads:
        newThread = threading.Thread(target=modules.frameExtract,args=(inputFile,n,),daemon=True)
        newThread.start()
        print("Begun extracting frame " + str(n))
        n = n+1

n = 0

while n < length+1:
    path = modules.tmpFolder + modules.upscaleFolder + str(n) + ".png"
    if threading.active_count()<threads:
        newThread = threading.Thread(target=modules.frameUpscale,args=(path,4,),daemon=True)
        newThread.start()
        print("Begun upscaling frame " + str(n))
        n = n+1