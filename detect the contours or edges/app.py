#Write a Program to detect the contours or edges in the photos




import os
import cv2
import numpy as np
from flask import Flask, request, send_file

app = Flask(__name__)

# Define Upload and Processed Folders
UPLOAD_FOLDER = "uploads"
PROCESSED_FOLDER = "processed"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_image():
    # Check if file is in request
    if "file" not in request.files:
        return "No file uploaded", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    # Save uploaded image
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Process the image (edge detection)
    processed_path = process_image(filepath)
    
    # Return the processed image
    return send_file(processed_path, mimetype="image/png")

def process_image(image_path):
    """Applies Canny Edge Detection and saves the processed image."""
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(img, 100, 200)  # Apply Canny edge detection

    # Save the processed image
    processed_path = os.path.join(PROCESSED_FOLDER, "edges_" + os.path.basename(image_path))
    cv2.imwrite(processed_path, edges)
    return processed_path

if __name__ == "__main__":
    app.run(debug=True)
