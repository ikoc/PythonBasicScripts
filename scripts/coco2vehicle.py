import os
from shutil import copyfile

idList = ['2','3','5','7']
nameList = ["car","motorbike","bus","truck"]
idMap = { '2':'0','3':'1','5':'2','7':'3'}

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def readDarknetLabelWithFilter(path,idList):
    with open(path) as f:
        lines = f.readlines()
    filteredLines = []
    for line in lines:
        parts = line.split(" ")
        id = parts[0]
        if id in idList:
            parts[0] = idMap[parts[0]]
            newline = " ".join(parts)
            filteredLines.append(newline)
    return filteredLines

def convert(inputPath,outputPath,idList):
    labels = os.listdir(inputPath)
    labels.sort()
    for count,labelName in enumerate(labels):
        print(count,labelName)
        labelPath = os.path.join(inputPath,labelName)
        outLabelPath = os.path.join(outputPath,labelName)
        filteredLines = readDarknetLabelWithFilter(labelPath,idList)
        if len(filteredLines) > 0:
            with open(outLabelPath,"w") as f:
                f.writelines(filteredLines)

def prepareTrainValTxt(trainPath,validPath):
    trainLabels = os.listdir(trainPath)
    validLabels = os.listdir(validPath)
    t = open("trainFiltered.txt","w")
    v = open("validFiltered.txt","w")
    for count,labelName in enumerate(trainLabels):
        path = os.path.join(trainPath,labelName)
        path = path.replace("txt","jpg").replace("labelsFiltered","images")
        if count % 25 == 0:
            v.write(path + "\n")
        else:
            t.write(path + "\n")
    for count,labelName in enumerate(validLabels):
        path = os.path.join(validPath,labelName)
        path = path.replace("txt","jpg").replace("labelsFiltered","images")
        if count % 25 == 0:
            v.write(path + "\n")
        else:
            t.write(path + "\n")

def copyFiles(inputTxt,outputFolder):
    with open(inputTxt) as f:
        lines = f.readlines()
        for line in lines:
            src = line.strip()
            dst = os.path.join(outputFolder,os.path.basename(src))
            copyfile(src, dst)
        

'''
inp = "labels/val2014"
out = "labelsFiltered/val2014"
convert(inp,out,idList)

inp = "labels/train2014"
out = "labelsFiltered/train2014"
convert(inp,out,idList)

trainPath = "labelsFiltered/val2014"
validPath = "labelsFiltered/train2014"
prepareTrainValTxt(trainPath,validPath)

inputTxt = "trainFiltered.txt"
outputFolder = "imagesFiltered/"
copyFiles(inputTxt,outputFolder)
inputTxt = "validFiltered.txt"
'''
