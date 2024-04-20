from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr_code', methods=['POST'])
def generate_qr_code():
    link = request.form['link']
    filename = request.form['filename']
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    
    # Create an in-memory bytes stream to store the QR code image
    qr_img_bytes = BytesIO()
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(qr_img_bytes, format='PNG')
    qr_img_bytes.seek(0)
    
    # Save QR code image to file
    filepath = os.path.join(os.getcwd(), f'{filename}.png')
    with open(filepath, 'wb') as f:
        f.write(qr_img_bytes.getvalue())
    
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
