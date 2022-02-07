#!/usr/bin/env python3
from PIL import Image
from sys import argv
def main():
  outputFile = "out.png"
  if (len(argv) > 3):
    outputFile = argv[3]
  rawData = open(argv[2], "rb")
  data = rawData.read()
  rawData.close()
  pixelList = []
  tempData = []
  print("Creating pixels...")

  for i in data:
    if (len(tempData) == 3):
      pixelList.append((tempData[0],tempData[1],tempData[2]))
      tempData = []
    tempData.append(i)
  if (len(tempData) > 0):
    for i in range(3 - len(tempData)):
      tempData.append(0)
    pixelList.append((tempData[0],tempData[1],tempData[2]))
  #gets closest whole number that makes a perfect square
  imgRes = int(-(-len(pixelList)**.5//1))
  print("Writing image...")
  img = Image.new('RGB', (imgRes, imgRes))
  img.putdata(pixelList)
  img.save(outputFile)

if __name__ == '__main__':
  main()