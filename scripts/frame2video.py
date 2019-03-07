import cv2
import os
import sys

imageFolder = "files"
imageList = os.listdir(imageFolder)
imageList.sort()

## get image sizes
img = cv2.imread(os.path.join(imageFolder,imageList[0])) 
size = (img.shape[1],img.shape[0])
outFps = 25

out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G') ,outFps,size)
totalImageNum = len(imageList)

for count,imgName in enumerate(imageList): 
    if count%100==0:
        print ("{}/{}".format(count,totalImageNum))
    imgPath = os.path.join(imageFolder,imgName)
    frame = cv2.imread(imgPath)
    out.write(frame)

out.release()
