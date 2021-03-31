import pyqrcode
url = pyqrcode.create(input("Enter URL\n"))
url.svg('Image.svg', scale=8)
print(url.terminal(quiet_zone=1))
