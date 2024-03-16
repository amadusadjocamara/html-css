"""import qrcode
img = qrcode.make(
    "google.com"
)
img.save("myQRcode.png")
img.show()"""
import qrcode

img = qrcode.make("google.com")
img.save("myQRcode.png")
img.show()
