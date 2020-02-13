#pip install pillow
#pip install pytesseract
#install tesseract-ocr exe / add to PATH

from PIL import Image
import pytesseract

# For 64-bit Windows_OS, add the following command to executable file
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

im = Image.open("download.jpg")

text = pytesseract.image_to_string(im, lang = 'eng')

result = 'opencv' in text

print(text)
print(result)