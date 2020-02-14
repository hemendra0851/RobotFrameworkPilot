#pip install pillow
#pip install pytesseract
#install tesseract-ocr exe / add to PATH

# ImageGrab-To capture the screen image in a loop.  
# Bbox used to capture a specific area.

from PIL import Image, ImageEnhance, ImageFilter
import pytesseract,os
import numpy as nm
import cv2

# For 64-bit Windows_OS, add the following command to executable file
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def getTextFromImg(imgPath):
	img = Image.open(imgPath)
	#imgText = pytesseract.image_to_string(img, lang='eng', config='--psm 6')
	imgText = pytesseract.image_to_string(cv2.cvtColor(cv2.imread(imgPath), cv2.COLOR_BGR2GRAY), lang ='eng')

	return imgText

def saveToFile(imgText):
	text_file = open("Output6.txt", "w")
	text_file.write(imgText)
	text_file.close()

def validateText(imgText, str):
	return str in imgText


imgPath = "img6.jpg"
#print(getTextFromImg(imgPath))
saveToFile(getTextFromImg(imgPath))
