import io
import requests
import pytesseract
from PIL import Image, ImageFilter, ImageEnhance


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

response = requests.get('https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTCs1qJ060oQztPgqd_2EMyRGKf5iT9Y9U8ZlFfBYNOdCFbdHVE')
img = Image.open(io.BytesIO(response.content))
img = img.convert('L')
img = img.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(2)
img = img.convert('1')
img.save('image.jpg')
imagetext = pytesseract.image_to_string(img)
print(imagetext)
