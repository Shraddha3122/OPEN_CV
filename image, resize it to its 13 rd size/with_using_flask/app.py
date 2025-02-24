from flask import Flask, send_file
import cv2
import numpy as np

app = Flask(__name__)

# Path to your image
IMAGE_PATH = "D:/WebiSoftTech/OPEN CV/image, resize it to its 13 rd size/with_using_flask/taj1.jpg"

@app.route('/')
def home():
    return "Go to /image to see the resized image."

@app.route('/image')
def serve_resized_image():
    # Read the image
    image = cv2.imread(IMAGE_PATH)

    if image is None:
        return "Error: Image not found!", 404

    # Get original dimensions
    height, width = image.shape[:2]

    # Resize to 1/3rd of the original size
    new_width, new_height = width // 3, height // 3
    resized_image = cv2.resize(image, (new_width, new_height))

    # Encode the image as JPEG
    _, buffer = cv2.imencode('D:/WebiSoftTech/OPEN CV/image, resize it to its 13 rd size/with_using_flask/taj1.jpg', resized_image)
    return send_file(
        io.BytesIO(buffer),
        mimetype='D:/WebiSoftTech/OPEN CV/image, resize it to its 13 rd size/with_using_flask/taj1.jpg',
        as_attachment=False
    )

if __name__ == '__main__':
    app.run(debug=True)
