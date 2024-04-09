import qrcode
from PIL import Image

# Create a QRCode object with customizable options:
qr = qrcode.QRCode(
    version=40,  # Adjust version for data capacity (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Set error correction level (L, M, Q, H)
    box_size=20,  # Set module size in pixels
    border=4,  # Set border width
)

# Add the data to be encoded:
qr.add_data("https://sites.google.com/view/sajalphys")  # Replace with your desired data

# Generate the QR code:
qr.make(fit=True)  # Efficiently utilize space

# Create a PIL image with preferred colors:
img = qr.make_image(fill_color="black", back_color="white")  # Customize colors as needed

# Save the QR code image:
img.save("mysite40.png")  # Set desired filename

