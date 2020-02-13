from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

im = Image.open("C:\\Users\\Hemendra Pratap\\Downloads\\download.jpg")

text = pytesseract.image_to_string(im, lang = 'eng')

result = 'Hemendra' in text

print(text)
print(result)