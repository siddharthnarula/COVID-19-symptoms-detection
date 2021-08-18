#import files and libraries
from PIL import Image
import cv2
import io
import os
import time
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
#define the image
img = cv2.imread("image1.jpg")
height = 240
width = 320
dim=(height,width)
res = cv2.resize(img,dim,interpolation = cv2.INTER_LINEAR)
#making image suitable for editing
blur = cv2.GaussianBlur(res,(5,5),0)
gray = cv2.cvtColor(blur, cv2.COLOR_RGB2GRAY)
display("image",gray)
cv2.imshow("image",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(res)
#extracting useful information
words = pytesseract.image_to_string(res,lang="eng")
name = words[62:74]
#export in csv file
import csv
import datetime
from datetime import date
today = date.today()
time=datetime.datetime.now()
namelist=[]
dateandtime=[]
namelist.append(name)
time=datetime.datetime.now()
current_day = time.strftime("%d/%m/%Y")
dateandtime.append(current_day)
current_time = time.strftime("%H:%M:%S")
dateandtime.append(current_time)
a=[]
a.append(name)
a.append(current_day)
a.append(current_time)
with open('name1.csv','a') as csvFile:
 writer =csv.writer(csvFile)
 writer.writerow(a)
