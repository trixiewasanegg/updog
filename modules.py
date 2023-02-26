import os
import cv2

tmpFolder = "tmp/"

def frameExtract(file):
    #Gets frames of file
    cv2vid = cv2.VideoCapture(file)
    frame_count = cv2vid.get(cv2.CAP_PROP_FRAME_COUNT)

    n = 0
    while frame_count > n+1:
        command = "ffmpeg -i " + file + " -vf \"select=eq(n\\," + str(n) + ")\" -vframes 1 " + tmpFolder + "raw" + str(n) + ".png"
        os.system(command)
        n = n+1