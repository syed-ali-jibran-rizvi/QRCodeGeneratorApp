# QR Code Generator

This is a simple Flask web application for generating QR codes. Users can input a link and a filename, and the application will generate a QR code for the provided link and allow users to download the QR code image with the specified filename.

## Prerequisites

- Python 3.x
- Flask
- qrcode

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/syed-ali-jibran-rizvi/QRCodeGeneratorApp.git
    ```

2. Navigate to the project directory:

    ```bash
    cd qr-code-generator
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
   
3. Enter the link and filename for the QR code you want to generate.

4. Click on the "Generate QR Code" button.

5. The QR code image will be generated, and you will be prompted to download it with the specified filename.


## File Structure

```
qr-code-generator/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── screenshots/
    ├── screenshot1.png
    └── screenshot2.png
```
