import qrcode
import qrcode.constants

def gen_qr_code(text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


if __name__ == "__main__":
    text = "Hello, this is a QR code generated using Python!"
    filename = "qr_code2.png"
    gen_qr_code(text, filename) 
    print(f"QR code generated and saved as {filename}.")