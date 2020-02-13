#pip install pillow
#pip install pytesseract
#install tesseract-ocr exe / add to PATH

from PIL import Image, ImageEnhance, ImageFilter
import pytesseract,os

# For 64-bit Windows_OS, add the following command to executable file
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

path= "img4.jpg"

text = pytesseract.image_to_string(Image.open(path), lang='eng',
                        config='--psm 6')
result = 'opencv' in text

print(text)
print(result)