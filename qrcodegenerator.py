import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, box_size=10, border=5)

data = "https://youtube.com"
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")

