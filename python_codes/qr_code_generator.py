import pyqrcode
from pyzbar.pyzbar import decode
from PIL import image

# Create the QR code
qr = pyqrcode.create("Coding with MzaCamp")
qr.png("myQrCode.png", scale=8)

# Read the QR Code
d = decode(Image.open("myQrCode.png"))
print(d[0].data.decode("ascii"))