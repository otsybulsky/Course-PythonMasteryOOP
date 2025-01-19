import qrcode
from qrcode.image.pure import PyPNGImage

def generate_qr_code(
        data, 
        file_name, 
        error_correction = qrcode.constants.ERROR_CORRECT_L, 
        box_size = 10,
        border = 4
        ):
    qr =  qrcode.QRCode(error_correction=error_correction,
                        box_size=box_size,
                         border=border)
    qr.add_data(data=data)
    qr.make(fit=True)
    img = qr.make_image(image_factory=PyPNGImage)
    img.save(file_name)

if __name__ == "__main__":
    generate_qr_code("https://example.com", "qr_code.png")