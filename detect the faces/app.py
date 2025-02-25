import os
import cv2
import numpy as np
from flask import Flask, request, send_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load OpenCV face detector (Haar Cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def detect_faces(image_path):
    """Detects faces in an image and saves the processed image."""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Save processed image
    output_path = os.path.join(app.config["UPLOAD_FOLDER"], "result.jpg")
    cv2.imwrite(output_path, img)

    return output_path

@app.route("/detect_faces", methods=["POST"])
def upload_file():
    """Handles image upload and face detection."""
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    image_path = os.path.join(app.config["UPLOAD_FOLDER"], "input.jpg")
    file.save(image_path)

    result_path = detect_faces(image_path)

    return send_file(result_path, mimetype="image/jpeg")

@app.route("/get_image/<filename>", methods=["GET"])
def get_image(filename):
    """Serves processed images."""
    image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    if not os.path.exists(image_path):
        return "File not found", 404
    return send_file(image_path, mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(debug=True)
