import os
import cv2

tmpFolder = "tmp/"
upscaleFolder = "up/"

commandRun = []
commandResult = []

def execute(command):
    try:
        commandRun.append(command)
        out = os.system(command)
        commandResult.append(out)
    except:
        print(command + " failed.")

def vidLen(file):
    #Gets frames of file
    cv2vid = cv2.VideoCapture(file)
    frame_count = cv2vid.get(cv2.CAP_PROP_FRAME_COUNT)
    return frame_count

def frameExtract(file,n):
    command = "ffmpeg -i " + file + " -vf \"select=eq(n\\," + str(n) + ")\" -vframes 1 " + tmpFolder + str(n) + ".png"
    execute(command)

def frameUpscale(imgIn, scale):
    command = "realsr-ncnn-vulkan.exe -i " + imgIn + " -o " + upscaleFolder + imgIn + " -s " + str(scale)
    execute(command)