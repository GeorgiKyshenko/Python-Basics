import pyqrcode

address = "https://www.mobile.bg/pcgi/mobile.cgi?act=4&adv=11679659717606773&slink=rv02jx"
url = pyqrcode.create(address)
url.png("car.png", scale=8)
