import qrcode

def create_qr_code(data, filename):
    img = qrcode.make(data)
    img.save(filename)
    print(f"Your QR code has been generated and saved as '{filename}'")
