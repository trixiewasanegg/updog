import os
import cv2

def getLen(file):
    video = cv2.VideoCapture(file)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    return frame_count

vid = "test-footage/test.mp4"
n = 0
outfolder = "out/"

print(getLen(vid))

while n < getLen(vid):
    command = "ffmpeg -i " + vid + " -vf \"select=eq(n\\," + str(n) + ")\" -vframes 1 " + outfolder + str(n) + ".png"
    os.system(command)
    n = n+1