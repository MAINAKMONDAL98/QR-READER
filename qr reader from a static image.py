from pyzbar.pyzbar import decode
from PIL import Image

#test.jpg is just a raw QR image from a generic QR generator
test = decode(Image.open('test.jpg'))

print(test)
