import cv2
import base64
from flask import Flask, render_template

app = Flask(__name__)

def encode_image(image):
    """Convert image to base64 encoding for HTML display."""
    _, buffer = cv2.imencode('D:/WebiSoftTech/OPEN CV/image as colored as well as black and white image/Using_flask/taj1.jpg', image)
    return base64.b64encode(buffer).decode('utf-8')

@app.route('/')
def index():
    # Read image in color
    color_image = cv2.imread('D:/WebiSoftTech/OPEN CV/image as colored as well as black and white image/Using_flask/taj1.jpg')

    # Read image in grayscale
    grayscale_image = cv2.imread('D:/WebiSoftTech/OPEN CV/image as colored as well as black and white image/Using_flask/taj1.jpg', cv2.IMREAD_GRAYSCALE)

    # Convert color image to RGB 
    color_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)

    # Encode images to base64
    color_encoded = encode_image(color_image)
    grayscale_encoded = encode_image(grayscale_image)

    return render_template('D:/WebiSoftTech/OPEN CV/image as colored as well as black and white image/Using_flask/templates/index.html', color_img=color_encoded, gray_img=grayscale_encoded)

if __name__ == '__main__':
    app.run(debug=True)
