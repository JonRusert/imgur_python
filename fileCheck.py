#!/usr/bin/python
import configparser
from imgurpython import ImgurClient
import datetime
import sys
from time import sleep
import os.path
import shutil

now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
if(day == 1): #need to update month and find which day NOTE:doesn't account for new year, nor leap year
    month -= 1
    if(month in [1, 3, 5, 7, 8, 10, 12]):
        day = 31
    if(month in [4, 6, 9, 11]):
        day = 30
    if(month == 2):
        day =28
else:
    day -=1
        
date = str(year) + "-" + str(month) + "-" + str(day)
date = "2017-11-9"
dateFile = "/home/ubuntu/imgur_python/galleryIds/" + date
images = open(dateFile, 'r')
outDateFile = "/home/ubuntu/imgur_python/galleryIdsCompleted/" + date
outImages = open(outDateFile, 'a')
dateFileNew = dateFile + "-new"
newImages = open(dateFileNew, 'w')

for image in images:

    image = image.rstrip()
    outImageFile = "/home/ubuntu/imgur_python/commentIds/" + date + "-" + str(image)
    if(os.path.exists(outImageFile)):
        outImages.write(image + "\n")
    else:
        newImages.write(image + "\n")
        
        
    

outImages.close()
newImages.close()
images.close()    

shutil.copy(dateFileNew, dateFile)
            
       
